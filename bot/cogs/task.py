import random
from datetime import datetime, timedelta

import config
from arena_bot import ArenaBot
from discord import Embed
from discord.ext.commands import Cog, CommandInvokeError, Context, group
from models import Player
from models import Task as TaskModel
from models import TaskProficiency, TaskType
from orm import NoMatch


class AlreadyOnTask(Exception):
    """Error raised when a user attempts to start a task while already on one."""""

    def __init__(self, task: TaskModel):
        self.task = task


class Task(Cog):
    """Cog holds Task commands"""

    def __init__(self, bot: ArenaBot):
        self.bot = bot

    async def cog_command_error(self, ctx: Context, error: CommandInvokeError):
        """Handle errors within the cog"""
        if isinstance(error.original, AlreadyOnTask):
            task = error.original.task
            if task.completion_date <= datetime.utcnow():
                embed = await self._task_completed(task)
            else:
                embed = await task.embed
            await ctx.reply(embed=embed)
        else:
            raise error

    @staticmethod
    async def _get_or_create_player_proficiency(user_id: int) -> TaskProficiency:
        """Get the player proficiency, if it doesn't exist one will be made."""
        player = await Player.objects.get(id=user_id)
        try:
            return await TaskProficiency.objects.get(player=player)
        except NoMatch:
            return await TaskProficiency.objects.create(player=player)

    @staticmethod
    def calculate_time(level: int) -> float:
        """
        Calculate the time the task will take based on level.

        :level: Proficiency level of the player
        :return: Time taken in minutes
        """
        output = config.TASK_BASE_TIME
        current_step = config.TASK_BASE_DECREASE
        for _ in range(level):
            output -= current_step
            current_step *= config.TASK_DECREASE_MULTI
        return max(config.TASK_BASE_TIME // 2, output)

    async def _task_completed(self, task: TaskModel) -> Embed:
        """This is called when a task is completed. Returns a relevant embed."""
        embed = Embed(title="Task Completed", colour=task.task_type.colour)

        # Update the users proficiency randomly for the task completed.
        player = task.player
        proficiency = await TaskProficiency.objects.get(player=player)
        await proficiency.increment_exp(
            task.task_type,
            random.randint(config.TASK_EXP_GAIN_MIN, config.TASK_EXP_GAIN_MAX)
        )
        await task.update(completed=True)

        reward = round(config.TASK_BASE_REWARD * (config.TASK_REWARD_MULTI * proficiency.task_level(task.task_type)))
        await player.load()
        await player.update(coin=player.coin + reward)
        embed.description = f"You received {reward} gold."

        return embed

    async def _create_task(self, user_id: int, task: TaskType) -> TaskModel:
        proficiency = await self._get_or_create_player_proficiency(user_id)
        task_level = proficiency.task_level(task)
        return await TaskModel.objects.create(
            player=proficiency.player,
            completion_date=datetime.utcnow() + timedelta(minutes=self.calculate_time(task_level)),
            _task_type=task.value,
        )

    @group()
    async def task(self, ctx: Context):
        """Task group. Sends current task if currently doing one, else send help message."""
        try:
            task = await TaskModel.objects.get(player=ctx.author.id, completed=False)
            raise AlreadyOnTask(task)

        except NoMatch:
            if ctx.invoked_subcommand is None:
                await ctx.reply("Task help message...")

    @task.command()
    async def hunt(self, ctx: Context):
        """Begin a hunt_exp."""
        task = await self._create_task(ctx.author.id, TaskType.Hunt)
        embed = await task.embed
        await ctx.reply(embed=embed)

    @task.command()
    async def mine(self, ctx: Context):
        """Begin a mining session."""
        task = await self._create_task(ctx.author.id, TaskType.Mine)
        embed = await task.embed
        await ctx.reply(embed=embed)

    @task.command()
    async def gather(self, ctx: Context):
        """Begin a gather_exp."""
        task = await self._create_task(ctx.author.id, TaskType.Gather)
        embed = await task.embed
        await ctx.reply(embed=embed)

    @task.command()
    async def lumber(self, ctx: Context):
        """Begin a woodcutting session."""
        task = await self._create_task(ctx.author.id, TaskType.Lumber)
        embed = await task.embed
        await ctx.reply(embed=embed)


def setup(bot: ArenaBot) -> None:
    """Add the cog to the bot"""
    bot.add_cog(Task(bot))


def teardown(bot: ArenaBot) -> None:
    """Remove the cog cleanly"""
    bot.remove_cog('Task')

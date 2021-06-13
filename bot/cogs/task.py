import random
from datetime import datetime, timedelta

from discord import DiscordException
from discord.ext.commands import Cog, Context, group, CommandInvokeError
from orm import NoMatch

import config
from arena_bot import ArenaBot
from models import Player, Task as TaskModel, TaskType, TaskProficiency


class AlreadyOnTask(DiscordException):
    """Error raised when a user attempts to start a task while already on one."""""
    def __init__(self, task: TaskModel):
        self.task = task


class Task(Cog):
    """Cog holds Task commands"""

    def __init__(self, bot: ArenaBot):
        self.bot = bot

    async def cog_command_error(self, ctx: Context, error: CommandInvokeError) -> None:
        """Handle errors within the cog"""
        if isinstance(error.original, AlreadyOnTask):
            task = error.original.task
            embed = await task.embed

            if task.completion_date <= datetime.utcnow():
                embed.description = "Task completed"

                # Update the users proficiency randomly for the task completed.
                proficiency = await TaskProficiency.objects.get(player=task.player)
                await proficiency.increment_exp(
                    task.task_type,
                    random.randint(config.TASK_EXP_GAIN_MIN, config.TASK_EXP_GAIN_MAX)
                )

                await task.update(completed=True)
            else:
                embed.description = f"Already on a task, finishing at {task.completion_date}"
            await ctx.send(embed=embed)

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

    async def _create_task(self, user_id: int, task: TaskType) -> TaskModel:
        proficiency = await self._get_or_create_player_proficiency(user_id)
        task_level = proficiency.task_level(task)
        print(task_level)

        return await TaskModel.objects.create(
            player=proficiency.player,
            completion_date=datetime.utcnow() + timedelta(seconds=5),
            _task_type=task.value,
        )

    @group()
    async def task(self, ctx: Context) -> None:
        """Task group. Sends current task if currently doing one, else send help message."""
        try:
            task = await TaskModel.objects.get(player=ctx.author.id, completed=False)
            raise AlreadyOnTask(task)

        except NoMatch:
            if ctx.invoked_subcommand is None:
                await ctx.send("Task help message...")

    @task.command()
    async def hunt(self, ctx: Context) -> None:
        """Begin a hunt_exp."""
        task = await self._create_task(ctx.author.id, TaskType.Hunt)
        embed = await task.embed
        await ctx.send(embed=embed)

    @task.command()
    async def mine(self, ctx: Context) -> None:
        """Begin a mining session."""
        task = await self._create_task(ctx.author.id, TaskType.Mine)
        embed = await task.embed
        await ctx.send(embed=embed)

    @task.command()
    async def gather(self, ctx: Context) -> None:
        """Begin a gather_exp."""
        task = await self._create_task(ctx.author.id, TaskType.Gather)
        embed = await task.embed
        await ctx.send(embed=embed)

    @task.command()
    async def lumber(self, ctx: Context) -> None:
        """Begin a woodcutting session."""
        task = await self._create_task(ctx.author.id, TaskType.Lumber)
        embed = await task.embed
        await ctx.send(embed=embed)


def setup(bot: ArenaBot) -> None:
    """Add the cog to the bot"""
    bot.add_cog(Task(bot))


def teardown(bot: ArenaBot) -> None:
    """Remove the cog cleanly"""
    bot.remove_cog('Task')

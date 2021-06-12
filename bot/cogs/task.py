from datetime import datetime, timedelta
from typing import Optional, Union

from discord import DiscordException, User, Member, Embed
from discord.ext.commands import Cog, Context, group, CommandInvokeError
from orm import NoMatch

from arena_bot import ArenaBot
from models import Player, Task as TaskModel, TaskType


class AlreadyOnTask(DiscordException):
    def __init__(self, task: TaskModel):
        self.task = task


class Task(Cog):
    """Cog holds Task commands"""

    def __init__(self, bot: ArenaBot):
        self.bot = bot

    async def cog_command_error(self, ctx: Context, error: CommandInvokeError) -> None:
        if isinstance(error.original, AlreadyOnTask):
            task = error.original.task
            embed = await task.embed

            if task.completion_date <= datetime.utcnow():
                embed.description = "Task completed"
                await task.update(completed=True)
            else:
                embed.description = f"Already on a task, finishing at {task.completion_date}"
            await ctx.send(embed=embed)

        else:
            raise error

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
        """Begin a hunt."""
        player = await Player.objects.get(id=ctx.author.id)

        task = await TaskModel.objects.create(
            player=player,
            completion_date=datetime.utcnow() + timedelta(minutes=1),
            _task_type=TaskType.Hunt.value,
        )
        embed = await task.embed
        await ctx.send(embed=embed)

    @task.command()
    async def mine(self, ctx: Context) -> None:
        """Begin a mining session."""
        player = await Player.objects.get(id=ctx.author.id)
        task = await TaskModel.objects.create(
            player=player,
            completion_date=datetime.utcnow() + timedelta(minutes=1),
            _task_type=TaskType.Mine.value,
        )
        embed = await task.embed
        await ctx.send(embed=embed)

    @task.command()
    async def gather(self, ctx: Context) -> None:
        """Begin a gather."""
        player = await Player.objects.get(id=ctx.author.id)
        task = await TaskModel.objects.create(
            player=player,
            completion_date=datetime.utcnow() + timedelta(minutes=1),
            _task_type=TaskType.Gather.value,
        )
        await ctx.send(embed=await task.embed)


def setup(bot: ArenaBot) -> None:
    """Add the cog to the bot"""
    bot.add_cog(Task(bot))


def teardown(bot: ArenaBot) -> None:
    """Remove the cog cleanly"""
    bot.remove_cog('Task')

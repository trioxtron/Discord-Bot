import discord
from discord.ext import commands
import mysqllib


class Board:
    def __init__(self):
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]


    def make_turn(self, cell, player):
        if self.is_valid_turn(cell):
            self.state[cell] = player.symbol
            return True
        return False


    def is_valid_turn(self, cell):
        if self.state[cell] == 0:
            return True
        else:
            return False


    def check_win(self, player):
        s = player.symbol
        if self.state[0] == s and self.state[1] == s and self.state[2] == s:
            return True
        elif self.state[3] == s and self.state[4] == s and self.state[5] == s:
            return True
        elif self.state[6] == s and self.state[7] == s and self.state[8] == s:
            return True

        elif self.state[0] == s and self.state[3] == s and self.state[6] == s:
            return True
        elif self.state[1] == s and self.state[4] == s and self.state[7] == s:
            return True
        elif self.state[2] == s and self.state[5] == s and self.state[8] == s:
            return True

        elif self.state[0] == s and self.state[4] == s and self.state[8] == s:
            return True
        elif self.state[2] == s and self.state[4] == s and self.state[6] == s:
            return True

    def print_board(self):
        return (f"```  {self.sign_to_printable(self.state[0])}  |  {self.sign_to_printable(self.state[1])}  |  {self.sign_to_printable(self.state[2])}  \n-----------------\n  {self.sign_to_printable(self.state[3])}  |  {self.sign_to_printable(self.state[4])}  |  {self.sign_to_printable(self.state[5])}  \n-----------------\n  {self.sign_to_printable(self.state[6])}  |  {self.sign_to_printable(self.state[7])}  |  {self.sign_to_printable(self.state[8])}```") 

    def is_full(self):
        for i in self.state:
            if i == 0:
                return False
        return True


    def sign_to_printable(self, sign):
        if sign == 0:
            return " "
        elif sign == 1:
            return "X"
        else:
            return "O"


class Player:
    def __init__(self, symbol):
        self.symbol = symbol



class TicTacToe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(help = "Die beiden Spieler spielen abwechselnd und schreiben jeweils den Standort, andem ihr Symbol gesetzt werden soll.\nAnordnung der Standorte:\n\n  1  |  2  |  3  \n-----------------\n  4  |  5  |  6  \n-----------------\n  7  |  8  |  9")
    async def ttt(self, ctx, opponent : discord.User):
        player1 = Player(1)
        player2 = Player(-1)
        user1 = ctx.author
        user2 = opponent

        board = Board()

        active_player = player1
        active_user = user1
        message = await ctx.send(board.print_board())
        while not board.is_full():
            
            await message.edit(content=board.print_board())

            try:
                cell = await self.bot.wait_for('message', check=lambda message: message.author == active_user, timeout=300.0)
                await cell.delete()
            except ValueError:
                continue
            cell = int(cell.content)

            cell = cell - 1
            if cell < 0 or cell > 8:
                await ctx.send("Die Zahl war nicht zwischen 1 und 9.")
                continue

            if not board.make_turn(cell, active_player):
                await ctx.send("Nicht möglich.")
                continue

            if board.check_win(active_player):
                await ctx.send(f"{active_user.mention} hat gewonnen.")
                await message.edit(content=board.print_board())


            else:
                pass

            if active_player == player1 and active_user == user1:
                active_player = player2
                active_user = user2
            else:
                active_player = player1
                active_user = user1

        await message.edit(content=board.print_board())



def setup(bot):
    bot.add_cog(TicTacToe(bot))

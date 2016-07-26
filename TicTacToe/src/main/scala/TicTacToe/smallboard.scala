package TicTacToe

case class SmallBoard(squares: Vector[Player]) extends GameProperties {

    override def toString: String = {
        def displayBoard(index: Int): String = {
            if (index == 8) squares(index) + " \n"
            else if (index % 3 == 2) squares(index) + " \n" + displayBoard(index + 1)
            else squares(index) + " " + displayBoard(index + 1)
        }
        displayBoard(0)
    }

    def makeMove(move: Int, pl: Player): SmallBoard = {
        SmallBoard(squares.updated(move, pl))
    }

    lazy val possibleMoves: List[Int] = {
        {for(i <- 0 until 9 if squares(i) == Empty) yield i}.toList
    }

    lazy val winner: Player = {
        def findWinner(combos: List[List[Int]], pl: Player): Boolean = {
            if (combos.isEmpty) false
            else if ((combos.head map (squares(_) == pl)) forall  (_ == true)) true
            else findWinner(combos.tail, pl)
        }

        if (findWinner(winningCombos, X)) X
        else if (findWinner(winningCombos, O)) O
        else Empty
    }

    lazy val isComplete: Boolean = {
        this.winner != Empty ||
        squares.indexOf(Empty) == -1
    }
}

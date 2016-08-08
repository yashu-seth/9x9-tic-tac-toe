package TicTacToe

case class BigBoard(boards: Vector[SmallBoard]) extends Board with GameProperties {

    override def toString: String = {
        def getSmallRow(board: SmallBoard, row: Int): String =
            board.squares(row * 3) + " " + board.squares(row * 3 + 1) + " " + board.squares(row * 3 + 2) + " "

        def getBigRow(bigrow: Int): String = {
            val big_board_id = (bigrow / 3) * 3

            getSmallRow(boards(big_board_id), bigrow % 3) + " " + getSmallRow(boards(big_board_id + 1), bigrow % 3) +
            " " + getSmallRow(boards(big_board_id + 2), bigrow % 3) + " "
        }

        def displayBoard(bigrow: Int): String = {
            if (bigrow == 8)
                getBigRow(bigrow) + "\n\n" + "===================" +"\n\n"
            else if (bigrow % 3 == 2)
                getBigRow(bigrow) + "\n\n" + displayBoard(bigrow + 1)
            else
                getBigRow(bigrow) + "\n" + displayBoard(bigrow + 1)
        }

        displayBoard(0)
    }

    def makeMove(move: Move, pl: Player): BigBoard = {
        BigBoard(boards.updated(move._1, boards(move._1).makeMove(move._2, pl)))
    }

    def availableSmallBoard(prevSmallMove: Int): List[SmallBoard] = {
        if (!boards(prevSmallMove).isComplete) List(boards(prevSmallMove))
        else {boards filter (x => !x.isComplete)}.toList
    }

    def possibleMoves(lastSmallMove: Int): List[Move] = {
        boards(lastSmallMove).possibleMoves map (x => (lastSmallMove, x))
    }

    lazy val winner: Player = {
        if (boards exists (x => x.winner == X)) X
        else if (boards exists (x => x.winner == O)) O
        else Empty
    }

    lazy val isComplete: Boolean = {
        winner != Empty
    }

}

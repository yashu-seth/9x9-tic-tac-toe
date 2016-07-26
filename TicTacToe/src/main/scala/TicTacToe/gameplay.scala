package TicTacToe

object PlayGame extends MiniMax {

    def main(args: Array[String]) = {

        def getHumanMove(board: SmallBoard, msg: String = ""): Int = {
            println(msg)
            val humanMove: Int = readInt()
            if (humanMove < 1 || humanMove > 9 || board.squares(humanMove - 1) != Empty) {
                println("Invalid Move, please enter a valid move.")
                getHumanMove(board)
            }
            else {
                println("Your move is "+ humanMove)
                humanMove
            }
        }

        println(EmptyBoard)
        val firstHumanMove: Int = getHumanMove(EmptyBoard, "Enter your first move.")
        playGame(EmptyBoard.makeMove(firstHumanMove - 1, computerPlayer.enemy))

        def playGame(board: SmallBoard): Unit = {

            println(board)

            if (board.winner != Empty) {
                println("The winner is " + board.winner)
            }

            else if (board.isComplete) {
                println("Its a DRAW.")
            }

            else {
                
                val optimalMove = getOptimalMove(board)

                val nextBoard = board.makeMove(optimalMove, computerPlayer)
                println(nextBoard)

                if (nextBoard.winner == computerPlayer) println("The winner is " + computerPlayer)
                else {
                    val humanMove: Int = getHumanMove(nextBoard, "Make your move.")
                    playGame(nextBoard.makeMove(humanMove - 1, computerPlayer.enemy))
                }
            }
        }
    }
}

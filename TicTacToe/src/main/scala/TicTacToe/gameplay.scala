package TicTacToe

object PlayGame extends MiniMax {

    def main(args: Array[String]) = {

        def getHumanMove(board: BigBoard, msg: String = ""): Move = {
            println(msg)
            val humanMove: Int = readInt()
            val humanMove2: Int = readInt()
            val move = (humanMove, humanMove2)
            // if (humanMove < 1 || humanMove > 9 || board.squares(humanMove - 1) != Empty) {
            //     println("Invalid Move, please enter a valid move.")
            //     getHumanMove(board)
            // }
            // else {
            println("Your move is "+ move)
            move
            // }
        }

        println(EmptyBigBoard)
        val firstHumanMove: Move = getHumanMove(EmptyBigBoard, "Enter your first move.")
        playGame(EmptyBigBoard.makeMove(firstHumanMove, computerPlayer.enemy), firstHumanMove._2)

        def playGame(board: BigBoard, lastSmallMove: Int): Unit = {

            println(board)

            if (board.winner != Empty) {
                println("The winner is " + board.winner)
            }

            else if (board.isComplete) {
                println("Its a DRAW.")
            }

            else {
                
                val optimalMove = getOptimalMove(board, lastSmallMove)

                val nextBoard = board.makeMove(optimalMove, computerPlayer)
                println(nextBoard)

                if (nextBoard.winner == computerPlayer) println("The winner is " + computerPlayer)
                else {
                    val humanMove: Move = getHumanMove(nextBoard, "Make your move.")
                    playGame(nextBoard.makeMove(humanMove, computerPlayer.enemy), humanMove._2)
                }
            }
        }
    }
}

package TicTacToe

import scala.util.Random

trait MiniMax extends GameProperties {

    val EmptyBoard = SmallBoard((1 to 9).toVector map (x => Empty))

    val EmptyBigBoard = BigBoard((1 to 9).toVector map (x => EmptyBoard))

    // lastSmallMove and depth default to -1 for the 3X3 game. They are used only in the
    // 9X9 game.
    def moveScore(board: Board, pl: Player, lastSmallMove: Int = -1, depth: Int = -1): Int = {

        if(depth==maxDepth) 0

        else if (board.isComplete) {
            if (board.winner == computerPlayer) 1
            else if (board.winner == computerPlayer.enemy) -1
            else 0
        }

        else {
            val futureMoveScores: List[Int] = board match {
                case SmallBoard(squares) => 
                    SmallBoard(squares).possibleMoves map (move =>
                                                           moveScore(SmallBoard(squares).makeMove(move, pl), pl.enemy))
                case BigBoard(boards) =>
                    BigBoard(boards).possibleMoves(lastSmallMove) map (move => 
                                                                       moveScore(BigBoard(boards).makeMove(move, pl),
                                                                       pl.enemy, move._2, depth+1))
            }

            if (pl == computerPlayer) futureMoveScores.max
            else futureMoveScores.min
        }
    }

    // For the 3X3 game
    def getOptimalMove(board: SmallBoard): Int = {
        val futureMoves: List[(Int,Int)] = 
            board.possibleMoves map (move => (move, moveScore(board.makeMove(move,
                                               computerPlayer), computerPlayer.enemy)))

        val maxScore = futureMoves.unzip._2.max
        // move_score is a pair of (move, score)
        val optimalMoves = for (move_score <- futureMoves
                                if move_score._2 == maxScore) yield move_score._1
        Random.shuffle(optimalMoves.toList).head
    }

    // For the 9X9 game
    def getOptimalMove(board: BigBoard, lastSmallMove: Int): Move = {
        val futureMoves: List[(Move, Int)] =
            board.possibleMoves(lastSmallMove) map (move => (move, moveScore(board.makeMove(move,
                                                                             computerPlayer),
                                                                             computerPlayer.enemy, 
                                                                             lastSmallMove, 0)))
        val maxScore = futureMoves.unzip._2.max
        val optimalMoves = for (move_score <- futureMoves
                                if move_score._2 == maxScore) yield move_score._1
        Random.shuffle(optimalMoves.toList).head
    }
}

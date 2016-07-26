package TicTacToe

import scala.util.Random

trait MiniMax extends GameProperties {

    val EmptyBoard = SmallBoard((1 to 9).toVector map (x => Empty))

    val EmptyBigBoard = BigBoard((1 to 9).toVector map (x => EmptyBoard))

    def moveScore(board: SmallBoard, pl: Player): Int = {
        if (board.isComplete) {
            if (board.winner == computerPlayer) 1
            else if (board.winner == computerPlayer.enemy) -1
            else 0
        }
        else {
            val futureMoveScores: List[Int] =
                board.possibleMoves map (move => moveScore(board.makeMove(move, pl), pl.enemy))
            if (pl == computerPlayer) futureMoveScores.max
            else futureMoveScores.min
        }
    }

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
}

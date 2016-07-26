package TicTacToe

trait Player {
    override def toString: String = this match {
        case Empty => "-"
        case X => "X"
        case O => "O"
    }

    def enemy: Player = this match {
        case Empty => Empty
        case X => O
        case O => X
    }
}

case object Empty extends Player
case object X extends Player
case object O extends Player


trait GameProperties {

    type Move = (Int, Int)

    val winningCombos = List(List(0, 1, 2), List(3, 4, 5),
                             List(6, 7, 8), List(0, 3, 6),
                             List(1, 4, 7), List(2, 5, 8),
                             List(0, 4, 8), List(2, 4, 6))

    val computerPlayer = X

}

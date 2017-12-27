
public class BoardGame extends Game {
	BoardGame(){
		System.out.println("Creating a board game, " + difficulty);
		name = "board game";
	}
	
	void placeBoard() {
		System.out.println("placing board for game: " + name);
	}
}

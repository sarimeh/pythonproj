
public class Game {
	String name = "Game of life";
	int difficulty;
	
	Game() {
		System.out.println("Creating a game");
		difficulty = 3;
	}
	
	public void start() {
		System.out.println("starting: " + name + ", " + difficulty);
	}
	
}

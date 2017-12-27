
public class Chess extends BoardGame {
	Chess() {
		name = "Chess";
		System.out.println("creating a chess game");
		difficulty = 5;
	}
	
	public void placeChessmen(){
		System.out.println("placing chessmen");
	}
	
	public void start() {
		System.out.println(name + ": whites move");
	}
}

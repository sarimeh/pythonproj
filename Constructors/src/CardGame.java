
public class CardGame extends Game {

	public void start(){
		shuffle();
		System.out.println("starting card game, " + difficulty);
	}
	
	public void shuffle(){
		System.out.println("shuffle cards, ");
	}
}

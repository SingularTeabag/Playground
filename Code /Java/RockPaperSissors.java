import java.util.Scanner;
class RockPaperSissors {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        int compMove = 0;

        String playerMove;

        System.out.println("Rock Paper Sissors\n");
        System.out.print("What will you play? ");

        playerMove = input.nextLine();
        playerMove = playerMove.toLowerCase();

        if(!(playerMove.equals("rock") || playerMove.equals("paper") || playerMove.equals("sissors"))) {
            System.out.println("You must chose Rock, Paper, or, Sissors");
        }

        compMove =  (int)(Math.random() * 3);
        System.out.println("compMove");
    }
}

import java.util.Scanner;
class RockPaperSissors {
    static Scanner input = new Scanner(System.in);
    public static void main(String[] args) {
        mainGame();
    }

    public static void mainGame() {
        int compMove = 0;
        int playerIntMove = 0;

        String playerMove;

        // 0 - rock, 1 - paper, 2 sissors
        System.out.println("Rock Paper Sissors\n");
        System.out.print("What will you play? ");

        playerMove = input.nextLine();
        playerMove = playerMove.toLowerCase();

        while(!(playerMove.equals("rock") || playerMove.equals("paper") || playerMove.equals("sissors"))) {
            System.out.println("You must chose Rock, Paper, or, Sissors");

            System.out.print("What will you play? ");
            playerMove = input.nextLine();
            playerMove = playerMove.toLowerCase();
        }

        compMove =  (int)(Math.random() * 3);
        System.out.println();

        if(playerMove.equals("rock")) {
            playerIntMove = 0;
        }
        else if (playerMove.equals("paper")) {
            playerIntMove = 1;
        }
        else {
            playerIntMove = 2;
        }

        //player plays rock
        if (playerIntMove == 0) {
            if(compMove == 0) {
                System.out.println("The computer plays Rock! \nTie!");
            }
            else if(compMove == 1) {
                System.out.println("The computer plays Paper! \nComputer wins!");
            }
            else 
                System.out.println("The computer plays Sissors! \nYou win!");
        }
        //player plays paper
        else if (playerIntMove == 1) {
            if(compMove == 0) {
                System.out.println("The computer plays Rock! \nYou win!");
            }
            else if(compMove == 1) {
                System.out.println("The computer plays Paper! \nTie!");
            }
            else 
                System.out.println("The computer plays Sissors! \nComputer wins!");
        }
        //player plays sissors
        else if (playerIntMove == 2) {
            if(compMove == 0) {
                System.out.println("The computer plays Rock! \nComputer wins!");
            }
            else if(compMove == 1) {
                System.out.println("The computer plays Paper! \nYou win!");
            }
            else 
                System.out.println("The computer plays Sissors! \nTie!");
        }

        playAgain();
    }

    public static void playAgain() {
        String playerAnswer;
        System.out.print("\nWould you like to play again? ");
        playerAnswer = input.nextLine();

        playerAnswer = playerAnswer.toLowerCase();

        if(playerAnswer.equals("yes") || playerAnswer.equals("y")) {
            mainGame();
        }
        else 
            System.exit(0);


    }
}
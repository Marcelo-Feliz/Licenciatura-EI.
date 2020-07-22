package pt.uevora;

import java.util.*;
import java.util.concurrent.TimeUnit;

public class Gestor
{

    private String username;
    private String password;
    private int grupo;
    

    public String getUserName() 
    {
        return username;
    }

    public void setUserName(String username) 
    {
        this.username = username;
    }

    public String getPassword() 
    {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public int getGrupo() {
        return grupo;
    }

    public void setGrupo(int grupo) {
        this.grupo = grupo;
    }
    
    public static void Menu(int id)
    {   
        System.out.println("1: Aprovar Férias");
        System.out.println("2: LogOut");
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();  // Read user input
        
        if (num == 1) 
        {
            
            gerirFerias(id);
            
        }
        else if (num == 2) 
        {
        	Main.Login();
        }

    }


    public static void gerirFerias(int id)
    {
        System.out.println("Periodos de Ferias em espera para aprovacao:");
        int n = 1;
        int a = 0;
        for(int i = 0; i< Main.periodosFerias.size(); i++)
		{	
			if (Main.gestorList.get(id).getGrupo() == Main.periodosFerias.get(i).getGrupo() && (Main.periodosFerias.get(i).getEstadoAtual().equals("Em aprovacao") == true)) {
                System.out.println(n +":"+Main.periodosFerias.get(i).getUserName()+":"+ Main.periodosFerias.get(i).getDataInicio()+"/"+Main.periodosFerias.get(i).getDataFim() );
                n++;
                a =1;
			}
			
			
        }
        if (a ==0) {
        	System.out.println("Nao tem nenhum periodo de ferias para aprovar");
        	Menu(id);
        }
        
        Scanner scanner = new Scanner(System.in);
        System.out.println( "Insira o ID do periodo de férias:");
        int number = scanner.nextInt();  // Read user input
        
        if (number > Main.periodosFerias.size() || number <= 0) {
        	System.out.println("ID não existe");
        	gerirFerias(id);
        }
        
        int count = 1;
        int pos = 0;

        for(int i = 0; i< Main.periodosFerias.size(); i++)
		{	
			if (Main.gestorList.get(id).getGrupo() == Main.periodosFerias.get(i).getGrupo() && (Main.periodosFerias.get(i).getEstadoAtual().equals("Em aprovacao") == true && count == number)) {
               pos = i;
            }
        
            

        }
        
        
        System.out.println("1: Aprovar");
        System.out.println("2: Rejeitar");
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();  // Read user input
        
        if (num == 1) 
        {
            System.out.println("O período de ferias foi aprovado com sucesso.");
            Main.periodosFerias.get(pos).setEstadoAtual("Aprovado");
            Menu(id);
          
            
        }
        else if (num == 2) 
        {
             System.out.println("O período de ferias foi rejeitado.");
             Main.periodosFerias.get(pos).setEstadoAtual("Rejeitado");
             
             int dias = Main.periodosFerias.get(pos).getDiasUteisUtilizados();
             for (int i = 0; i< Main.colaboradorList.size(); i++) {
            	 
            	 if (Main.colaboradorList.get(i).getUserName().equals(Main.periodosFerias.get(pos).getUserName()) == true) {
            		 Main.colaboradorList.get(i).setDiasFeriasRestantes(Main.colaboradorList.get(i).getDiasFeriasRestantes() + dias);
                  }
             }
             for (int i = 0; i< Main.periodosFerias.size(); i++) {
            	 if(Main.periodosFerias.get(i).getEstadoAtual().equals("Rejeitado") == true) {
            		 Main.removeColaborador(i); 
            	 }
             }
             
             Menu(id);
        }
    }
}
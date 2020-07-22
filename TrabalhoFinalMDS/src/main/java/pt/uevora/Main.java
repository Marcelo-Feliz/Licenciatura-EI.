package pt.uevora;

import java.util.*;
import pt.uevora.*;



public class Main 
{
	static List<Colaborador>  colaboradorList;
    static List<Gestor>  gestorList;
    static List<Colaborador> periodosFerias = new LinkedList();

    public static void main(String[] args)
    {   
    	initializeC();
    	initializeG();
    	
    
        
        Login();
    } 
    
    public static void Login(){
        int Login = 0;
        int indexuser = -1;
        
   
        while(Login == 0){
   
        	
            Scanner myObj = new Scanner(System.in);
            System.out.println( "Insira o seu nome de utilizador:");
            String user = myObj.nextLine();  // Read user input
            

            Scanner myObj2= new Scanner(System.in);
            System.out.println( "Insira a sua password:");
            String pass = myObj2.nextLine();

            
            
            Colaborador c = new Colaborador();
            Gestor g = new Gestor();
            
            List<Colaborador>  colaboradorList = new LinkedList();
            colaboradorList = findAllc();
            
            List<Gestor>  gestorList = new LinkedList();
            gestorList = findAllg();


            for(int i = 0; i< colaboradorList.size(); i++)
            {	
            	if (user.compareTo(colaboradorList.get(i).getUserName()) == 0 && pass.compareTo(colaboradorList.get(i).getPassword()) == 0) {
                	indexuser = i;
                }
            }
            if (indexuser >-1) {
            	Login = 1; 
        		
        		c.Menu(indexuser); //manda para menu do colaborador
            }
            indexuser = -1;
            
            

            for(int i = 0; i< gestorList.size(); i++)
            {		
            	if (user.compareTo(gestorList.get(i).getUserName()) == 0 && pass.compareTo(gestorList.get(i).getPassword()) == 0) {
                	indexuser = i;
            	}
            }
            if (indexuser >-1) {
            	Login = 1; 
        		
        		g.Menu(indexuser); //manda para menu do gestor
            }
            if(Login == 0){
                System.out.println("Nome de utilizador ou password errado"); 
            }     
        }
    }
    public static void initializeC()
    {
    	
        colaboradorList = new LinkedList();

        String [] trabalhadores = 
        {
            "Colaborador1 abc1 1 22 0",
            "Colaborador2 abc2 1 22 0",
            "Colaborador3 abc3 1 22 0", 
            "Colaborador4 abc4 1 22 0", 
            "Colaborador5 abc5 1 22 0", 
            "Colaborador6 abc6 2 22 0", 
            "Colaborador7 abc7 2 22 0", 
            "Colaborador8 abc8 2 22 0", 
            "Colaborador9 abc9 2 22 0",
            "Colaborador10 abc10 2 22 0"
        };
        
        
        for(String name: trabalhadores)
        {
            String [] parts = name.split(" ");
            String username = parts[0];
            String password = parts[1];
            String g = parts[2];
            String d = parts[3];
            String p = parts[4];
            int grupo = Integer.parseInt(g);
            int dias = Integer.parseInt(d);
            int pontuacao = Integer.parseInt(p);
            Colaborador colaborador = new Colaborador();
            colaborador.setUserName(username);
            colaborador.setPassword(password);
            colaborador.setGrupo(grupo);
            colaborador.setDiasFeriasRestantes(dias);
            colaborador.setPontuacao(pontuacao);
            
            addColaborador(colaborador); 
        }
    }
    
    public static void addColaborador(Colaborador colaborador)
    {
        colaboradorList.add(colaborador);
    }

    public static List<Colaborador> findAllc() 
    {
        return colaboradorList;
    }
    
    public static void initializeG()
    {

        gestorList = new LinkedList();

        String [] trabalhadores = 
        {
            "Gestor1 def1 1",
            "Gestor2 def2 2",
            
        };
        
        
        for(String name: trabalhadores)
        {
            String [] parts = name.split(" ");
            String username = parts[0];
            String password = parts[1];
            String g = parts[2];
            int grupo = Integer.parseInt(g);

            Gestor gestor = new Gestor();
            gestor.setUserName(username);
            gestor.setPassword(password);
            gestor.setGrupo(grupo);

            addGestor(gestor);
        }
  
    }

    public static void addGestor(Gestor gestor){
        gestorList.add(gestor);
    }


    public static List<Gestor> findAllg() {
        return gestorList;
    }

    public static void addColaborador2(Colaborador colaborador)
    {
        Main.periodosFerias.add(colaborador);
    }

    public static List<Colaborador> findAll2() 
    {
        return Main.periodosFerias;
    }
    
   
    public static void removeColaborador(int index)
    {
        Main.periodosFerias.remove(index);
    }

}

package pt.uevora;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mock;
import org.mockito.junit.MockitoJUnitRunner;
import static org.junit.Assert.*;
import static org.mockito.Mockito.when;

import java.util.LinkedList;
import java.util.List;



import pt.uevora.Gestor;



public class GestorTest 
{
  
    @Test
    public void test_Username() 
    {    
      Gestor gestor = new Gestor();
      gestor.setUserName("Gestor1");

		  assertEquals("Gestor1",gestor.getUserName());
    }
    
    @Test
    public void test_Password() 
    {    
      Gestor gestor = new Gestor();
      gestor.setPassword("def1");

		  assertEquals("def1",gestor.getPassword());
    }

    @Test
    public void test_Grupo() 
    {    
      Gestor gestor = new Gestor();
      gestor.setGrupo(1);

		  assertEquals(1,gestor.getGrupo());
    }

    @Test
    public void test_Gestor()
    { 
      Gestor gestor = new Gestor();
      List<Gestor>  gestorList;
      gestorList = new LinkedList();
      gestor.setUserName("Gestor1");
      gestor.setPassword("def1");
      gestor.setGrupo(1);

      
      
      gestorList.add(gestor);

      assertEquals(gestor.getUserName(), gestorList.get(0).getUserName());

    }


    @Test
    public void test_addGestor2()
    { 
      Gestor gestor = new Gestor();
      List<Gestor>  gestorList;
      gestorList = new LinkedList();
      gestor.setUserName("Gestor1");
      gestor.setPassword("def1");
      gestor.setGrupo(1);
      gestorList.add(gestor);

      Gestor gestor2 = new Gestor();
      gestor2.setUserName("Gestor2");
      gestor2.setPassword("gestor2");
      gestor2.setGrupo(1);
      gestorList.add(gestor2);

      assertEquals(gestor2.getUserName(), gestorList.get(1).getUserName());
    }
}

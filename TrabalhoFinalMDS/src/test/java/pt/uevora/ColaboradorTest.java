package pt.uevora;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mock;
import org.mockito.junit.MockitoJUnitRunner;
import static org.junit.Assert.*;
import static org.mockito.Mockito.when;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.LinkedList;
import java.util.List;



import pt.uevora.Colaborador;



public class ColaboradorTest 
{
  
    @Test
    public void test_Username() 
    {    
      Colaborador colaborador = new Colaborador();
      colaborador.setUserName("Colaborador1");

		  assertEquals("Colaborador1",colaborador.getUserName());
    }
    
    @Test
    public void test_Password() 
    {    
      Colaborador colaborador = new Colaborador();
      colaborador.setPassword("abc1");

		  assertEquals("abc1",colaborador.getPassword());
    }

    @Test
    public void test_Grupo() 
    {    
      Colaborador colaborador = new Colaborador();
      colaborador.setGrupo(1);

		  assertEquals(1,colaborador.getGrupo());
    }

    @Test
    public void test_DiasFeriasRestantes() 
    {    
      Colaborador colaborador = new Colaborador();
      colaborador.setDiasFeriasRestantes(22);

		  assertEquals(22,colaborador.getDiasFeriasRestantes());
    }


    @Test
    public void test_addColaborador()
    { 
      Colaborador colaborador = new Colaborador();
      List<Colaborador>  colaboradorList;
      colaboradorList = new LinkedList();
      colaborador.setUserName("Colaborador1");
      colaborador.setPassword("abc1");
      colaborador.setGrupo(1);
      colaborador.setDiasFeriasRestantes(22);

      colaboradorList.add(colaborador);

      assertEquals(colaborador.getUserName(), colaboradorList.get(0).getUserName());

    }


    @Test
    public void test_addColaborador2()
    { 
      Colaborador colaborador = new Colaborador();
      List<Colaborador>  colaboradorList;
      colaboradorList = new LinkedList();
      colaborador.setUserName("Colaborador1");
      colaborador.setPassword("abc1");
      colaborador.setGrupo(1);
      colaboradorList.add(colaborador);
      colaborador.setDiasFeriasRestantes(22);


      Colaborador colaborador2 = new Colaborador();
      colaborador2.setUserName("Colaborador2");
      colaborador2.setPassword("abc2");
      colaborador2.setGrupo(1);
      colaboradorList.add(colaborador2);
      colaborador.setDiasFeriasRestantes(22);


      assertEquals(colaborador2.getUserName(), colaboradorList.get(1).getUserName());

    }

    @Test
    public void test_Pontuacao() 
    {    
      Colaborador colaborador = new Colaborador();
      colaborador.setPontuacao(20);

		  assertEquals(20,colaborador.getPontuacao());
    }

    @Test
    public void test_DataInicio() 
    {    
      Colaborador colaborador = new Colaborador();

      SimpleDateFormat dateFormat = new SimpleDateFormat("dd-MM-yyyy");
      String h ="04-07-2019";
      Date dataInicio = null;
      try {
              //Parsing the String
          dataInicio = dateFormat.parse(h);
      } catch (ParseException e) {
          // TODO Auto-generated catch block
          e.printStackTrace();
      }

      colaborador.setDataInicio(dataInicio);

      SimpleDateFormat dateFormat2 = new SimpleDateFormat("dd-MM-yyyy");
      String h2 ="04-07-2019";
      Date dataI = null;
      try {
              //Parsing the String
          dataI = dateFormat.parse(h);
      } catch (ParseException e) {
          // TODO Auto-generated catch block
          e.printStackTrace();
      }

		  assertEquals(dataI,colaborador.getDataInicio());
    }
    @Test
    public void test_Fim() 
    {    
      Colaborador colaborador = new Colaborador();

      SimpleDateFormat dateFormat = new SimpleDateFormat("dd-MM-yyyy");
      String h ="04-07-2019";
      Date dataFim = null;
      try {
              //Parsing the String
          dataFim = dateFormat.parse(h);
      } catch (ParseException e) {
          // TODO Auto-generated catch block
          e.printStackTrace();
      }


      colaborador.setDataInicio(dataFim);


      SimpleDateFormat dateFormat2 = new SimpleDateFormat("dd-MM-yyyy");
      String h2 ="04-07-2019";
      Date dataF = null;
      try {
              //Parsing the String
          dataF = dateFormat.parse(h);
      } catch (ParseException e) {
          // TODO Auto-generated catch block
          e.printStackTrace();
      }


		  assertEquals(dataF,colaborador.getDataInicio());
    }


    @Test
    public void test_EstadoAtual() 
    {    
      Colaborador colaborador = new Colaborador();
      colaborador.setEstadoAtual("Aprovado");

		  assertEquals("Aprovado",colaborador.getEstadoAtual());
    }

    @Test
    public void test_DiasUteisUtilizados() 
    {    
      Colaborador colaborador = new Colaborador();
      colaborador.setDiasUteisUtilizados(20);

		  assertEquals(20,colaborador.getDiasUteisUtilizados());
    }



}

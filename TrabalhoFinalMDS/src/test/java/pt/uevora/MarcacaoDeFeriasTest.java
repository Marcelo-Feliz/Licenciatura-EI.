package pt.uevora;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mock;
import org.mockito.junit.MockitoJUnitRunner;
import static org.junit.Assert.*;
import static org.mockito.Mockito.when;

import java.util.Date;
import java.util.LinkedList;
import java.util.List;


import java.text.*;
import java.util.*;
import java.util.concurrent.TimeUnit;




import pt.uevora.MarcacaoDeFerias;;



public class MarcacaoDeFeriasTest 
{   
    

    @Test
    public void test_dataValida()
    { 
        SimpleDateFormat dateFormat = new SimpleDateFormat("dd-MM-yyyy");
        String h ="04-07-2019";
        Date date = null;
        try {
                //Parsing the String
            date = dateFormat.parse(h);
        } catch (ParseException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }


      assertTrue(MarcacaoDeFerias.dataValida(date));
    }
  
    @Test
    public void test_dataValida2()
    { 
        SimpleDateFormat dateFormat = new SimpleDateFormat("dd-MM-yyyy");
        String h ="04-07-2019";
        Date date = null;
        try {
                //Parsing the String
            date = dateFormat.parse(h);
        } catch (ParseException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        SimpleDateFormat dateFormat2 = new SimpleDateFormat("dd-MM-yyyy");
        String h2 ="07-07-2019";
        Date date2 = null;
        try {
                //Parsing the String
            date2 = dateFormat2.parse(h);
        } catch (ParseException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }


      assertTrue(MarcacaoDeFerias.dataValida2(date,date2));
    }
  

}

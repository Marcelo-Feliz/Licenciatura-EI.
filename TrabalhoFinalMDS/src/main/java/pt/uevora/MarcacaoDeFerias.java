
package pt.uevora;

import static org.mockito.ArgumentMatchers.anyIterableOf;
import static org.mockito.ArgumentMatchers.booleanThat;

import java.text.*;
import java.util.*;
import java.util.concurrent.TimeUnit;

public class MarcacaoDeFerias
{
	public static void MarcarFerias(int id) 
	{	
		Date dataI = null;
		Date dataF = null;

		
		Scanner scanner = new Scanner(System.in);
    	System.out.println( "Insira a data de inicio(dd-MM-yyyy):");
		String data = scanner.next();
		SimpleDateFormat dateFormat = new SimpleDateFormat("dd-MM-yyyy");
		Date dataInicio = null;
		try {
			//Parsing the String
			dataInicio = dateFormat.parse(data);
		} catch (ParseException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		boolean flag = dataValida(dataInicio);
		if(flag == true)
		{
			dataI = dataInicio;
		}
		else {
			System.out.println("Data invalida");
			Colaborador.Menu(id);
		}
		
		
		Scanner scanner2 = new Scanner(System.in);
    	System.out.println( "Insira a data de fim(dd-MM-yyyy):");
		String data2 = scanner.next();
		SimpleDateFormat dateFormat2 = new SimpleDateFormat("dd-MM-yyyy");
		Date dataFim = null;
		try {
			//Parsing the String
			dataFim = dateFormat2.parse(data2);
		} catch (ParseException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		boolean flag2 = dataValida2(dataI,dataFim);
		if(flag2 == true)
		{
			
			dataF = dataFim;
		}
		else{
			System.out.println("Data invalida");
			Colaborador.Menu(id);
		}
		
		Calendar calendario = Calendar.getInstance();
		int dias = 0;
		int pontuacao = 0;
		long diff = dataF.getTime() - dataI.getTime();
		dias = (int) TimeUnit.DAYS.convert(diff, TimeUnit.MILLISECONDS);
		dias ++;
		int diasFS = 0;
		calendario.setTime(dataI);
		int diasemana;
		
		for(int i = 0; i< Main.periodosFerias.size(); i++)
		{	
			
			if ( dataI.after(Main.periodosFerias.get(i).getDataInicio())  && dataF.before(Main.periodosFerias.get(i).getDataFim())  && (Main.periodosFerias.get(i).getUserName().equals(Main.colaboradorList.get(id).getUserName()) == true)) {
				System.out.println("Data Inavalida(ja existe um periodo de ferias marcado nessa altura)");
				Colaborador.Menu(id);
			}
			
			if ( dataI.before(Main.periodosFerias.get(i).getDataInicio())  && dataF.after(Main.periodosFerias.get(i).getDataInicio())  && (Main.periodosFerias.get(i).getUserName().equals(Main.colaboradorList.get(id).getUserName()) == true)) {
				System.out.println("Data Inavalida(ja existe um periodo de ferias marcado nessa altura)");
				Colaborador.Menu(id);
			}
			
			if ( dataI.before(Main.periodosFerias.get(i).getDataFim())  && dataF.after(Main.periodosFerias.get(i).getDataFim())  && (Main.periodosFerias.get(i).getUserName().equals(Main.colaboradorList.get(id).getUserName()) == true)) {
				System.out.println("Data Inavalida(ja existe um periodo de ferias marcado nessa altura)");
				Colaborador.Menu(id);
			}
			if ( dataI.before(Main.periodosFerias.get(i).getDataInicio())  && dataF.after(Main.periodosFerias.get(i).getDataFim())  && (Main.periodosFerias.get(i).getUserName().equals(Main.colaboradorList.get(id).getUserName()) == true)) {
				System.out.println("Data Inavalida(ja existe um periodo de ferias marcado nessa altura)");
				Colaborador.Menu(id);
			}

		}
	
		for (int i = 0; i < dias ;i++ ) {
			
			if(calendario.get(Calendar.DAY_OF_WEEK) == 1 || calendario.get(Calendar.DAY_OF_WEEK) == 7) {
				diasFS ++;	
			}
			else {
				if(calendario.get(Calendar.MONTH) == 0 || calendario.get(Calendar.MONTH) == 1 || calendario.get(Calendar.MONTH) == 10){
					pontuacao = pontuacao + 1;
				}
				if(calendario.get(Calendar.MONTH) == 2 || calendario.get(Calendar.MONTH) == 3 || calendario.get(Calendar.MONTH) == 4 || calendario.get(Calendar.MONTH) == 9){
					pontuacao = pontuacao + 2;
				}
				if(calendario.get(Calendar.MONTH) == 5 || calendario.get(Calendar.MONTH) == 8){
					pontuacao = pontuacao + 3;
				}
				if(calendario.get(Calendar.MONTH) == 6 || calendario.get(Calendar.MONTH) == 7 || calendario.get(Calendar.MONTH) == 11){
					pontuacao = pontuacao + 4;
				}
	
			}
			calendario.add(Calendar.DAY_OF_MONTH, +1);
		}
		dias = dias - diasFS;

		if (dias> Main.colaboradorList.get(id).getDiasFeriasRestantes()) {
			System.out.println("O colaborador já não têm dias suficientes disponíveis para poder marcar o período indicado.");
			Colaborador.Menu(id);
		}
		else {
			System.out.println("Numero de dias uteis: "+ dias);
			System.out.println("Pontuação: "+ pontuacao);
			
			Main.colaboradorList.get(id).setDiasFeriasRestantes(Main.colaboradorList.get(id).getDiasFeriasRestantes() - dias);
			Main.colaboradorList.get(id).setPontuacao(Main.colaboradorList.get(id).getPontuacao() + pontuacao);
			
			System.out.println("Dias restantes: "+ Main.colaboradorList.get(id).getDiasFeriasRestantes());
			System.out.println("O pedido encontra-se a aguardar pelo aprovação do gestor responsável");
			

			Colaborador colaborador = new Colaborador();
            colaborador.setUserName(Main.colaboradorList.get(id).getUserName());
            colaborador.setGrupo(Main.colaboradorList.get(id).getGrupo());
			colaborador.setDataInicio(dataI);
			colaborador.setDataFim(dataF);
			colaborador.setEstadoAtual("Em aprovacao");
			colaborador.setDiasUteisUtilizados(dias);
            
			
            Main.addColaborador2(colaborador); 

			Colaborador.Menu(id);
		}
	}


	public static void ConsultarFerias(int id) {
		int vazio = 0;
		System.out.println("Periodos de Ferias em espera para aprovacao:");

		for(int i = 0; i< Main.periodosFerias.size(); i++)
		{	
			if (Main.colaboradorList.get(id).getUserName() == Main.periodosFerias.get(i).getUserName() && (Main.periodosFerias.get(i).getEstadoAtual().equals("Em aprovacao") == true)) {
				System.out.println(Main.periodosFerias.get(i).getDataInicio()+"/"+Main.periodosFerias.get(i).getDataFim() );
			vazio = 1;
			}
			
		}
		if (vazio == 0) {
			System.out.println("Sem Periodos de Ferias em espera para aprovacao");
		}
		vazio = 0;
		
		System.out.println("Periodos de Ferias aprovados:");

		for(int i = 0; i< Main.periodosFerias.size(); i++)
		{	
			
			if (Main.colaboradorList.get(id).getUserName() == Main.periodosFerias.get(i).getUserName() && (Main.periodosFerias.get(i).getEstadoAtual().equals("Aprovado") == true)) {
				System.out.println(Main.periodosFerias.get(i).getDataInicio()+"/"+Main.periodosFerias.get(i).getDataFim() );
				vazio = 1;
			}
		}
		if (vazio == 0) {
			System.out.println("Sem Periodos de Ferias aprovados");
		}
		System.out.println("Dias restantes: "+ Main.colaboradorList.get(id).getDiasFeriasRestantes());
		Colaborador.Menu(id);
	}


	public static Boolean dataValida(Date dataInicio)
	{
		SimpleDateFormat dateFormat = new SimpleDateFormat("dd-MM-yyyy");
		boolean flag = false;
		String h ="30-06-2019";
		Date hoje = null;
		try {
			//Parsing the String
			hoje = dateFormat.parse(h);
		} catch (ParseException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		boolean after = dataInicio.after(hoje);
		
		if (after == true)
		{
			flag = true;
		}
		
		return flag;
	}
	public static Boolean dataValida2(Date dataInicio, Date dataFim)
	{
		boolean flag = false;
		boolean after = dataFim.after(dataInicio);
		
		
		
		if (after == true)
		{
			flag = true;
		}
		else if (dataFim.compareTo(dataInicio) == 0) {
			flag = true;
		}
		
		return flag;
	}
	
    
}
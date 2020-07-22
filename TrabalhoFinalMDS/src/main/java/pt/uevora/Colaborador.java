package pt.uevora;

import java.util.*;


public class Colaborador
{

    private String username;
    private String password;
    private int grupo;
    private int diasFeriasRestantes;
    private int pontuacao;
    private Date dataInicio;
    private Date dataFim;
    private String estadoAtual;
    private int dias;

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

    public void setPassword(String password) 
    {
        this.password = password;
    }


    public int getGrupo() 
    {
        return grupo;
    }

    public void setGrupo(int grupo) 
    {
        this.grupo = grupo;
    }

    public int getDiasFeriasRestantes()
    {
        return diasFeriasRestantes;
    }

    public void setDiasFeriasRestantes(int diasFeriasRestantes)
    {
        this.diasFeriasRestantes = diasFeriasRestantes;
    }

    public int getPontuacao()
    {
        return pontuacao;
    }

    public void setPontuacao(int pontuacao)
    {
        this.pontuacao = pontuacao;
    }
    public Date getDataInicio()
    {
        return dataInicio;
    }

    public void setDataInicio(Date dataInicio)
    {
        this.dataInicio = dataInicio;
    }

    public Date getDataFim()
    {
        return dataFim;
    }

    public void setDataFim(Date dataFim)
    {
        this.dataFim = dataFim;
    }
    public String getEstadoAtual()
    {
        return estadoAtual;
    }

    public void setEstadoAtual(String estadoAtual)
    {
        this.estadoAtual = estadoAtual;
    }


    public static void Menu(int id)
    {   
        System.out.println("1: Marcar Férias");
        System.out.println("2: Consultar Férias");
        System.out.println("3: LogOut");
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();  // Read user input
        
        if (num == 1) 
        {
        	MarcacaoDeFerias.MarcarFerias(id); // manda para a MarcacaoDeFerias
            
            
        }
        else if (num == 2) 
        {
            MarcacaoDeFerias.ConsultarFerias(id); // manda para a MarcacaoDeFerias
        }
        
        else if (num == 3) 
        {
            Main.Login();
        }

    }

	public void setDiasUteisUtilizados(int dias) {
		this.dias = dias;
		
	}
	public int getDiasUteisUtilizados() {
		return dias;
	}
    



}
from scipy.stats import (
    levene,
    mannwhitneyu,
    ttest_ind
)

def tabela_distribuicao_frequencias(dataframe, coluna, coluna_frequencia=False):
    """Cria uma tabela de distribuição de frequências para a coluna de um dataframe.
    Espera uma coluna categórica.
    
    Parameters
    ----------
    dataframe : pd.DataFrame
        Dataframe com os dados.
    coluna : str
        Nome da coluna categórica.
    coluna_frequencia : bool
        Informa se a coluna passada já é com os valores de frequência ou não. Padrão: False.
        
    Returns
    -------
    pd.DataFrame
        Dataframe com a tabela de distribuição de frequências.
    """    

def analise_levene(dataframe, alfa=0.05, centro="mean"):
    
    print("Tesde de Levene")
    
    estatistica_levene, valor_p_levene = levene(
        *[dataframe[coluna] for coluna in dataframe.columns],
        center=centro,
        nan_policy="omit"
    )
    
    print(f"{estatistica_levene=:.3f}")
    if valor_p_levene > alfa:
        print(f"Variâncias iguais (valor p: {valor_p_levene:.3f})")
    else:
        print(f"Ao menos uma variância diferente (valor p: {valor_p_levene:.3f})")

#==============================================================================================================================================================================

def analise_ttest_ind(
    dataframe,
    alfa=0.05,
    variancias_iguais=True,
    alternativa="two-sided",
):

    print("Teste t de Student")

    estatistica_ttest, valor_p_ttest = ttest_ind(
        *[dataframe[coluna] for coluna in dataframe.columns],
        equal_var=variancias_iguais,
        alternative=alternativa,
        nan_policy="omit"
    )
    
    print(f"{estatistica_ttest=:.3f}")
    if valor_p_ttest > alfa:
        print(f"Não rejeita a hipótese nula (valor p: {valor_p_ttest:.3f})")
    else:
        print(f"Rejeita a hipótese nula (valor p: {valor_p_ttest:.3f})")

#================================================================================================================================================================================

def analise_mannwhitneyun(
    dataframe,
    alfa=0.05,
    alternativa="two-sided",
):
    print("Teste de Mann-Whitney")

    estatistica_mannwhitneyu, valor_p_mannwhitneyu = mannwhitneyu(
        *[dataframe[coluna] for coluna in dataframe.columns],
        nan_policy="omit",
        alternative=alternativa
    )
    
    print(f"{estatistica_mannwhitneyu=:.3f}")
    if valor_p_mannwhitneyu > alfa:
        print(f"Não rejeita a hipótese nula (valor p: {valor_p_mannwhitneyu:.3f})")
    else:
        print(f"Rejeita a hipótese nula (valor p: {valor_p_mannwhitneyu:.3f})")

#=====================================================================================================================================================================================

def remove_outliers(dados, largura_bigodes=1.5):
    q1 = dados.quantile(0.25)
    q3 = dados.quantile(0.75)
    iqr = q3 - q1
    return dados[(dados >= q1 - largura_bigodes * iqr) & (dados <= q3 + largura_bigodes * iqr)]
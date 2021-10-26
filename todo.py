import pandas as pd


# Test 0
def numRows(games):
    """The number of rows in the games table.

    Parameters
    ----------
    games: DataFrame
        The table with results from Olympic Games, organized by country.
    """
    
    return games.index.size


# Test 1
def numColumns(games):
    """The number of columns in the games table.

    Parameters
    ----------
    games: DataFrame
        The table with results from Olympic Games, organized by country.
    """

    return games.columns.size


# Test 2
def numGoldTotal(games):
    """The total number of gold medals in any olympic game.

    The total number of gold medals includes the total number of gold medals
    in the summer and in the winter olympic games. All the countries must be
    considered, when computing this total.

    Parameters
    ----------
    games: DataFrame
        The table with results from Olympic Games, organized by country.
    """

    return games[ 'GoldT' ].sum()


# Test 3
def numSummerGoldCountry(games, country):
    """The number of gold medals won by country in the summer olympics.

    Parameters
    ----------
    games: DataFrame
        The table with results from Olympic Games, organized by country.
    games: str
        The country that we are considering in this query.
    """
   
    countryLine = games[ (games['Country'] == country) ]
    return countryLine.iloc[ 0 ][ 'GoldS' ]


# Test 4
def getCodeMaxSummerGold(games):
    """The code of the country with the most golds in the summer olympics.

    The country code is a string formed by three upper-case letters, in the
    'Code' column of the input table. We are interested in just one code: the
    code of the country that won more golds.

    Parameters
    ----------
    games: DataFrame
        The table with results from Olympic Games, organized by country.
    """
    
    idCountryMax = games[ 'GoldS' ].idxmax()
    return games.iloc[idCountryMax]['Code']


# Test 5
def getNthBestSummerCountry(games, n):
    """The N-th country in the rank of the summer olympics.

    Countries must be ordered first by the number of gold medals; then by the
    number of silver medals, and then by the number of bronze medals. If the
    countries have the same number of gold, silver and bronze medals, then
    they are ordered alphabetically.

    Parameters
    ----------
    games: DataFrame
        The table with results from Olympic Games, organized by country.
    n: int
        The index that we want in the rank.
    """

    tabelaOrdenada = games.sort_values( by=['GoldS', 'SilverS', 'BronzeS', 'Country'], \
                                        ascending=[False, False, False, True] )
    return tabelaOrdenada.iloc[n]['Country']


# Test 6
def numCountriesWithMoreThanNWinterMedals(games, n):
    """The number of countries that won strictly more than n medals of any kind.

    We are interested in only countries that won _more_ than n medals. This
    total considers gold, silver and bronze medals. We consider only medals in
    the Winter Olympics.

    Parameters
    ----------
    games: DataFrame
        The table with results from Olympic Games, organized by country.
    n: int
        The number of medals that we consider as a threshold.
    """

    return games.apply( lambda x: x['TotalW'] > n, axis=1 ).sum()
    

# Test 7
def numWinterCountries(games):
    """The number of countries that won more than average in the winter games.

    A Winter Country is a country that won more gold medals than the average
    number of gold medals won in the winter olympics. We are considering
    strictly more gold medals, meaning that if a country won exactly the
    average, then it is not a winter country.

    Parameters
    ----------
    games: DataFrame
        The table with results from Olympic Games, organized by country.
    """

    media = games[ 'GoldW' ].mean()
    return games.apply( lambda x: x['GoldW'] > media, axis=1 ).sum()


# Test 8
def countGoldsWithLetter(games, c):
    """Number of gold medals won by countries that start with a given letter.

    This function filters out the countries that start with a given letter,
    and then count the number of gold medals won by those countries in the
    Summer Olympics.

    Parameters
    ----------
    games: DataFrame
        The table with results from Olympic Games, organized by country.
    c: str
        The letter that must start the name of the countries that are
        considered.
    """

    def countGold( s ):
        if s['Country'][0] == c.upper():
            return s[ 'GoldS' ]

    return int(games.apply( countGold, axis=1 ).sum())
    

# Test 9
def countHybernalCountries(games):
    """Num of countries with no less medals in the winter games.

    This function counts the number of countries that won more (or the same
    number) total medals in the winter olympics than in the summer olympics.
    Remember: equality is not strict. Countries that won the same number of
    medals in both olympics are considered hybernal countries.

    Parameters
    ----------
    games: DataFrame
        The table with results from Olympic Games, organized by country.
    """

    hybernal = lambda x: x[ 'TotalW' ] >= x[ 'TotalS' ]
    return games.apply( hybernal, axis=1 ).sum()


# Careegando a tabela de jogos
tabelaDeJogos = pd.read_csv( 'games.csv' )

print( '\n\n' )

print( 'Número de linhas: ', numRows(tabelaDeJogos) )

print( 'Número de Colunas: ', numColumns(tabelaDeJogos) )

print( 'Número total de medalhas de ouro: ', numGoldTotal(tabelaDeJogos) )

print( 'Número de medalhas de ouro em jogos de verão do Brazil: ', numSummerGoldCountry(tabelaDeJogos, 'Brazil') )

print( 'País com maior número de GoldS: ', getCodeMaxSummerGold(tabelaDeJogos) )

print( 'Enésimo pais com no quadro de madalhas de verão: ', getNthBestSummerCountry(tabelaDeJogos, 20) )

print( 'Número de países com mais do que n winter medalhas: ', numCountriesWithMoreThanNWinterMedals(tabelaDeJogos, 10) )

print( 'countGoldsWithLetter a: ', countGoldsWithLetter(tabelaDeJogos, 'a') )
print( 'countGoldsWithLetter d: ', countGoldsWithLetter(tabelaDeJogos, 'd') )

print( 'Hybernal: ', countHybernalCountries(tabelaDeJogos) )



print( '\n\n' )

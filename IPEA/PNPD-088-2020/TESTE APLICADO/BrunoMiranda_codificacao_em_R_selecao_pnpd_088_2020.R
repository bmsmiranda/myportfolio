#  Seleção PNPD 088-2020  
#  Autor/Candidato: Bruno Miranda (bmsmiranda@gmail.com)
#  Github: https://github.com/bmsmiranda/myportfolio/tree/main/IPEA
#  Data: 
#    09-10-2020 - criação do script

#  Análise de resgistros em base fictícia Ipea 2020
#  Objetivo: responder questionamentos do teste aplicado

library(DBI)
library(dplyr)
library(ggplot2)
library(tidyverse)
library(readxl)
library(sqldf)
# ------------------------------------------------------------------------------

# Conexão ao banco
con <- DBI::dbConnect(odbc::odbc(), 
  .connection_string = "Driver={SQL Server Native Client 11.0};
                        Server=MSSQL2016\\DEFAULT;
                        Database=BANCO;
                        Trusted_Connection=yes;", timeout = 10)

# Querys ao banco
qry.evolucao.genero <- "select ano, sexo, count(*) as qtd from teste where ano between '1985' and '2019' and (sexo is not null and sexo != '') group by ano, sexo"
qry.segmento.raca <- "select raca, count(*) as qtd from teste where ano between '1985' and '2019' and (sexo is not null and sexo != '') and (raca is not null and raca != '') group by raca"
qry.salario.genero.F <- "select ano, sexo, AVG(CONVERT(numeric(8, 1), remuneracao)) as mediaremuneracao from teste where sexo = 'F' and ano between '2009' and '2019' and (sexo is not null and sexo != '') group by ano, sexo"
qry.salario.genero.M <- "select ano, sexo, AVG(CONVERT(numeric(8, 1), remuneracao)) as mediaremuneracao from teste where sexo = 'M' and ano between '2009' and '2019' and (sexo is not null and sexo != '') group by ano, sexo"

# Recupera valores do dataset
df.evolucao.genero <- DBI::dbGetQuery(con, qry.evolucao.genero)
df.segmento.raca <- DBI::dbGetQuery(con, qry.segmento.raca)
df.salario.genero.F <- DBI::dbGetQuery(con, qry.salario.genero.F)
df.salario.genero.M <- DBI::dbGetQuery(con, qry.salario.genero.M)

# Teste Aplicado (PNPD 088-2020)
# Graf: Média de remuneração segmentado pela variável sexo

# Reliza merge dos dataframes
df.media.remuneracao.merged <- merge(df.salario.genero.F, df.salario.genero.M, 
  by.x = "ano", by.y = "ano")
cores <- c("Masculino" = "dark blue", "Feminino" = "dark red")

grp.line.core.fc <- ggplot(df.media.remuneracao.merged, aes(x = ano)) + 
  geom_line(
    aes(y = mediaremuneracao.x,  color = "Masculino"),  
    size = 1.5, group = 1
  ) + 
  geom_line(
    aes(y = mediaremuneracao.x, color = "Feminino"), 
    size = 1.5, group = 1, linetype="twodash"
  ) +
  scale_y_continuous(labels = scales::number_format())

grp.line.core.fc + labs(x = "Período", y = "Mil Reais",
  title    = "Média de remuneração segmentado pela variável sexo",
  subtitle = "Período de análise: 2009 a 2019",
  caption  = "Fonte: Base Fictícia Ipea 2020",
  color    = "Legenda") +
  scale_color_manual(values = cores) +
  theme(
    plot.title   = element_text(color = "black", size = 16, face = "bold"),
    axis.title.x = element_text(size = 14, face = "bold"),
    axis.title.y = element_text(size = 14, face = "bold"),
    axis.text.y = element_text(size = 12, face = "bold"),
    axis.text.x = element_text(size = 12, face = "bold")
  )
# -----------------------------------------------------------------------------

# Teste Aplicado (PNPD 088-2020)
# Graf: Distribuição dos funcionários por raça
df.segmento.raca$perc <- round(
  (df.segmento.raca$qtd / sum(df.segmento.raca$qtd) * 100), 3)

perc.formatado <- paste(df.segmento.raca$raca, df.segmento.raca$perc, sep = " : ")
df.segmento.raca$racaperc <- paste(perc.formatado, "%", sep = "")
df.segmento.raca

grp.pie <- ggplot(data = df.segmento.raca) +
  geom_bar(aes(x = "", y = qtd, fill = racaperc), 
    stat = "identity", width = 1) +
  coord_polar("y", start = 0) +
  theme_void() +
  geom_text(
    aes(x = 1, y = (cumsum(qtd) - qtd / 2), 
      label = "")
  ) +
  labs(
    x = "X", y = "Y",
    fill = "raca",
    title = "Distribuição dos funcionários por raça",
    subtitle = "Período de análise: 1985 a 2019",
    caption  = "Fonte: Base Fictícia Ipea 2020"
  ) +
  theme(
    plot.title = element_text(color = "black", size = 16, face = "bold"),
    axis.text.y = element_text(size = 12, face = "bold")
  )
grp.pie

# -----------------------------------------------------------------------------

# Teste Aplicado (PNPD 088-2020)
# Graf: Quantitativo de funcionários categorizado por sexo e segmentado por ano
grp.barras <- ggplot(df.evolucao.genero, 
  aes(x = fct_reorder(ano, sexo), y = qtd, 
      fill = sexo)) +
  geom_col() + 
  scale_y_continuous(labels = scales::number_format()) +
  labs(
    x = "Ano", y = "Qtd.Funcionários",
    title = "Quantitativo de funcionários categorizado por sexo e segmentado por ano",
    subtitle = "Período de análise: 1985 a 2019",
    caption = "Fonte: Base Fictícia Ipea 2020"
  ) +
  theme(
    plot.title   = element_text(color = "black", size = 16, face = "bold"),
    axis.title.x = element_text(size = 14, face = "bold"),
    axis.title.y = element_text(size = 14, face = "bold"),
    axis.text.x = element_text(size = 12, face = "bold", angle = 45, hjust = 1),
    axis.text.y = element_text(size = 12, face = "bold")
  )

grp.barras
# -----------------------------------------------------------------------------

# Desconecta do banco de dados
DBI::dbDisconnect(con)

#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew_deploy.crew import CrewDeploy

# Essa linha diz ao Python para ignorar avisos do tipo SyntaxWarning 
# (avisos de sintaxe) que venham do módulo chamado pysbd.
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Este arquivo principal serve como uma maneira de você gerenciar sua
# equipe localmente, portanto, evite adicionar lógica desnecessária a este arquivo.
# Substitua pelas entradas que você deseja testar, pois ele irá interpolar automaticamente
# quaisquer informações sobre tarefas e agentes

def run():
    """
    Run the crew.
    """

    # Cria um dicionário chamado inputs com dois dados, ou seja, com os dados das chaves
    # que serão enviados como parametros para o programa ( apara os agentes e as tarefas)

    # --  'topic': define o assunto como "AI LLMs" (Modelos de Linguagem de Inteligência Artificial).
    # --  'current_year': pega o ano atual e transforma em string, usando datetime.now().year.
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    
    try:
        # Executa a crewAI passando dicionário  inputs como parametro
        CrewDeploy().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

# ------------------------------------------------------------------------------------

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        CrewDeploy().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

# -------------------------------------------------------------------------------------

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CrewDeploy().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


# --------------------------------------------------------------------------------------

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        CrewDeploy().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

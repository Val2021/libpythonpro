from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido
import pytest


def test_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize("destinatario",["renzo@python.pro.br","foo@bar.com.br"])
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(destinatario,
                                "luciano@python.pro.br",
                                "Cursos python pro",
                                "Primeira turma Guido Von Rossum aberta."
                                )

    assert destinatario in resultado


@pytest.mark.parametrize("remetente",
                         ["",
                         "renzo"])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
         enviador.enviar(
          remetente,
          "luciano@python.pro.br",
          "Cursos python pro",
          "Primeira turma Guido Von Rossum aberta."
         )



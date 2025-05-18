#kenobi/tests/preview_email.py

import os
import webbrowser
from kenobi.dtos.response_dto import ResponseDTO
from kenobi.services.email_service import build_email_html

def generate_test_opportunities():
    """Generate sample DTOs for testing the email template."""
    return [
        ResponseDTO(
            title="Programa de Inovação Tecnológica",
            resume="Apoio a projetos de inovação no setor industrial.",
            publication_date="10/03/2025",
            deadline="30/06/2025",
            funding_source="Finep, BNDES",
            target_audience="Empresas",
            theme="Indústria 4.0",
            link="http://finep.gov.br/edital-001",
            status="Active"
        ),
        ResponseDTO(
            title="Pesquisa em Saúde Pública",
            resume="Financiamento de pesquisas para melhorias no SUS.",
            publication_date="01/02/2025",
            deadline="15/05/2025",
            funding_source="Finep, Ministério da Saúde",
            target_audience="ICTs, Universidades",
            theme="Saúde",
            link="http://finep.gov.br/edital-002",
            status="Closed"
        ),
         ResponseDTO(
            title="AÇÃO CONJUNTA DE FOMENTO FINEP -BNDES",
            resume="Fomento conjunto entre Finep e BNDES.",
            publication_date="10/03/2025",
            deadline="30/06/2025",
            funding_source="Finep, BNDES",
            target_audience="Empresas",
            theme="Indústria 4.0",
            link="http://finep.gov.br/edital-001",
            status="Active"
        ),
        ResponseDTO(
            title="Programa Mulheres Inovadoras - 6ª edição",
            resume="Apoiar inovação liderada por mulheres.",
            publication_date="01/02/2025",
            deadline="15/05/2025",
            funding_source="Finep",
            target_audience="Empresas",
            theme="Saúde",
            link="http://finep.gov.br/edital-002",
            status="Closed"
        ),
         ResponseDTO(
            title="PRÓ-INFRA CENTROS TEMÁTICOS - Implantação e melhoria da infraestrutura de pesquisa para solucionar desafios em áreas temáticas críticas",
            resume="Melhoria da infraestrutura de pesquisa.",
            publication_date="10/03/2025",
            deadline="03/05/2024",
            funding_source="FNDCT",
            target_audience="Empresas",
            theme="Indústria 4.0",
            link="http://finep.gov.br/edital-001",
            status="Closed"
        ),
        ResponseDTO(
            title="4a Chamada Pública Conjunta entre Finep e RCN",
            resume="Parceria entre Finep e RCN.",
            publication_date="01/02/2025",
            deadline="15/05/2025",
            funding_source="FINEP; RCN; FNDCT",
            target_audience="ICTs, Universidades",
            theme="Saúde",
            link="http://finep.gov.br/edital-002",
            status="Closed"
        )
    ]

def preview_email():
    """Generate and open the email template in the browser for design preview."""
    subject = "Skip Financial Letter - Preview"
    opportunities = generate_test_opportunities()

    # Build HTML content
    html_content = build_email_html(opportunities, subject)

    # Save to file
    preview_file = os.path.abspath("kenobi/tests/email_preview.html")
    with open(preview_file, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"✅ Preview saved: {preview_file}")
    webbrowser.open(f"file://{preview_file}")

if __name__ == "__main__":
    preview_email()

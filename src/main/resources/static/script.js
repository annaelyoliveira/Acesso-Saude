async function buscar() {

    const cidade = document.getElementById("cidade").value;
    const bairro = document.getElementById("bairro").value;
    const tipo = document.getElementById("tipo").value;
    const turno = document.getElementById("turno").value;
    const nome = document.getElementById("nome").value;

    let url = "http://localhost:8080/api/v1/saude/unidades?";

    if (cidade) {
        url += `cidade=${cidade}&`;
    }

    if (bairro) {
        url += `bairro=${bairro}&`;
    }

    if (tipo) {
        url += `tipo=${tipo}&`;
    }

    if (turno) {
        url += `turno=${turno}&`;
    }

    if (nome) {
        url += `nome=${nome}&`;
    }

    const resposta = await fetch(url);

    const dados = await resposta.json();

    renderizarCards(dados);
}

function renderizarCards(unidades) {

    const resultado = document.getElementById("resultado");

    if (unidades.length === 0) {

        resultado.innerHTML = `
            <p class="sem-resultado">
                Nenhuma unidade encontrada.
            </p>
        `;

        return;
    }

    let html = "";

    unidades.forEach(unidade => {

        html += `

        <div class="card-unidade">

            <h2>
                ${unidade.nomeFantasia ?? "NÃO INFORMADO"}
            </h2>

            <div class="info">
                <strong>Tipo:</strong>
                ${unidade.tipoUnidadeDescricao ?? "NÃO INFORMADO"}
            </div>

            <div class="info">
                <strong>Turno:</strong>
                ${unidade.turnoDescricao ?? "NÃO INFORMADO"}
            </div>

            <div class="info">
                <strong>Telefone:</strong>
                ${unidade.telefone ?? "Não informado"}
            </div>

            <div class="info">
                <strong>Email:</strong>
                ${unidade.email ?? "Não informado"}
            </div>

            <div class="info">
                <strong>Endereço:</strong>

                ${unidade.endereco?.logradouro ?? ""},

                ${unidade.endereco?.numero ?? "S/N"}

                -

                ${unidade.endereco?.bairro ?? ""}

                -

                ${unidade.endereco?.cidade?.nome ?? ""}
            </div>

            <div class="capacidades">

                <h3>Capacidades</h3>

                <div class="grid-capacidades">

                    <div class="capacidade">
                        Centro Cirúrgico:
                        ${unidade.capacidade?.temCentroCirurgico ? "Sim" : "Não"}
                    </div>

                    <div class="capacidade">
                        Centro Obstétrico:
                        ${unidade.capacidade?.temCentroObstetrico ? "Sim" : "Não"}
                    </div>

                    <div class="capacidade">
                        Centro Neonatal:
                        ${unidade.capacidade?.temCentroNeonatal ? "Sim" : "Não"}
                    </div>

                    <div class="capacidade">
                        Atendimento Hospitalar:
                        ${unidade.capacidade?.temAtendimentoHospitalar ? "Sim" : "Não"}
                    </div>

                    <div class="capacidade">
                        Serviço Apoio:
                        ${unidade.capacidade?.temServicoApoio ? "Sim" : "Não"}
                    </div>

                    <div class="capacidade">
                        Atendimento Ambulatorial:
                        ${unidade.capacidade?.temAtendimentoAmbulatorial ? "Sim" : "Não"}
                    </div>

                </div>

            </div>

        </div>
        `;
    });

    resultado.innerHTML = html;
}
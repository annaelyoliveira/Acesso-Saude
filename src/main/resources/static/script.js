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

            <p class="info">
                <strong>Tipo:</strong>
                ${unidade.tipoUnidadeDescricao ?? "NÃO INFORMADO"}
            </p>

            <p class="info">
                <strong>Turno:</strong>
                ${unidade.turnoDescricao ?? "NÃO INFORMADO"}
            </p>

            <p class="info">
                <strong>Telefone:</strong>
                ${unidade.telefone ?? "Não informado"}
            </p>

            <p class="info">
                <strong>Email:</strong>
                ${unidade.email ?? "Não informado"}
            </p>

            <p class="info">
                <strong>Endereço:</strong>

                ${unidade.endereco?.logradouro ?? ""},

                ${unidade.endereco?.numero ?? "S/N"}

                -

                ${unidade.endereco?.bairro ?? ""}

                -

                ${unidade.endereco?.cidade?.nome ?? ""}
            </p>

            <div class="capacidades">

                <h3>Capacidades</h3>

                <div class="capacidades-grid">

                    <div class="capacidade">
                        Centro Cirúrgico:
                        ${unidade.capacidade?.stCentroCirurgico ? "Sim" : "Não"}
                    </div>

                    <div class="capacidade">
                        Centro Obstétrico:
                        ${unidade.capacidade?.stCentroObstetrico ? "Sim" : "Não"}
                    </div>

                    <div class="capacidade">
                        Centro Neonatal:
                        ${unidade.capacidade?.stCentroNeonatal ? "Sim" : "Não"}
                    </div>

                    <div class="capacidade">
                        Atendimento Hospitalar:
                        ${unidade.capacidade?.stAtendHospitalar ? "Sim" : "Não"}
                    </div>

                    <div class="capacidade">
                        Serviço Apoio:
                        ${unidade.capacidade?.stServicoApoio ? "Sim" : "Não"}
                    </div>

                    <div class="capacidade">
                        Atendimento Ambulatorial:
                        ${unidade.capacidade?.stAtendAmbulatorial ? "Sim" : "Não"}
                    </div>

                </div>

            </div>

            <details class="profissionais">

                <summary>
                    Ver profissionais
                </summary>

                ${
            unidade.profissionais &&
            unidade.profissionais.length > 0

                ?

                unidade.profissionais.map(profissional => `

                        <div class="profissional-item">

                            👨‍⚕️ ${profissional.nome}

                        </div>

                    `).join("")

                :

                `<p>Nenhum profissional encontrado.</p>`
        }

            </details>

        </div>
        `;
    });

    resultado.innerHTML = html;
}
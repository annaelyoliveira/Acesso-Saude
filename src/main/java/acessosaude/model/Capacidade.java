package acessosaude.model;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "\"tb_capacidades\"")
@Data
public class Capacidade {
    @Id
    @Column(name = "\"ID_ENDERECO\"")
    private Long idEndereco;

    @Column(name = "\"ST_CENTRO_CIRURGICO\"")
    private boolean temCentroCirurgico;

    @Column(name = "\"ST_CENTRO_OBSTETRICO\"")
    private boolean temCentroObstetrico;

    @Column(name = "\"ST_CENTRO_NEONATAL\"")
    private boolean temCentroNeonatal;

    @Column(name = "\"ST_ATEND_HOSPITALAR\"")
    private boolean temAtendimentoHospitalar;

    @Column(name = "\"ST_SERVICO_APOIO\"")
    private boolean temServicoApoio;

    @Column(name = "\"ST_ATEND_AMBULATORIAL\"")
    private boolean temAtendimentoAmbulatorial;
}
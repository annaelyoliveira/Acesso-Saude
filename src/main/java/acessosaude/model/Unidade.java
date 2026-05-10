package acessosaude.model;

import jakarta.persistence.*;
import lombok.Data;
import com.fasterxml.jackson.annotation.JsonProperty;

@Entity
@Table(name = "\"tb_unidades\"")
@Data
public class Unidade {
    @Id
    @Column(name = "\"CO_CNES\"")
    private String coCnes;

    @Column(name = "\"NO_FANTASIA\"")
    private String nomeFantasia;

    @Column(name = "\"TP_UNIDADE\"")
    private Long tipoUnidade;

    @Column(name = "\"NU_TELEFONE\"")
    private String telefone;

    @Column(name = "\"NO_EMAIL\"")
    private String email;

    @Column(name = "\"CO_TURNO_ATENDIMENTO\"")
    private Integer coTurno;

    @OneToOne
    @JoinColumn(name = "\"ID_ENDERECO\"", referencedColumnName = "\"ID_ENDERECO\"")
    private Endereco endereco;

    @OneToOne
    @JoinColumn(name = "\"ID_ENDERECO\"", referencedColumnName = "\"ID_ENDERECO\"", insertable = false, updatable = false)
    private Capacidade capacidade;

    // Comentado até que você rode o script de profissionais
    /*
    @ManyToMany
    @JoinTable(
        name = "tb_profissional_unidade",
        joinColumns = @JoinColumn(name = "CO_CNES"),
        inverseJoinColumns = @JoinColumn(name = "CO_PROFISSIONAL_SUS")
    )
    private List<Profissional> profissionais;
    */

    @JsonProperty("tipoUnidadeDescricao")
    public String getTipoUnidadeDescricao() {

        return switch (this.tipoUnidade.intValue()) {
            case 1 -> "POSTO DE SAÚDE";
            case 2 -> "CENTRO DE SAÚDE / UBS";
            case 4 -> "POLICLÍNICA";
            case 5 -> "HOSPITAL GERAL";
            case 7 -> "HOSPITAL ESPECIALIZADO";
            case 20 -> "PRONTO ATENDIMENTO";
            default -> "NÃO INFORMADO";
        };
    }

    @JsonProperty("turnoDescricao")
    public String getTurnoDescricao() {

        return switch (this.coTurno) {
            case 1 -> "MANHÃ";
            case 2 -> "TARDE";
            case 3 -> "MANHÃ E TARDE";
            case 4 -> "NOITE";
            case 5 -> "INTEGRAL";
            default -> "NÃO INFORMADO";
        };
    }
}
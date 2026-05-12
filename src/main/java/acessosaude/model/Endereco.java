package acessosaude.model;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "\"tb_enderecos\"")
@Data
public class Endereco {
    @Id
    @Column(name = "\"ID_ENDERECO\"")
    private Long id;

    @Column(name = "\"NO_LOGRADOURO\"")
    private String logradouro;

    @Column(name = "\"NU_ENDERECO\"")
    private String numero;

    @Column(name = "\"NO_BAIRRO\"")
    private String bairro;

    @ManyToOne
    @JoinColumn(name = "\"CO_IBGE\"", referencedColumnName = "\"CO_IBGE\"")
    private Cidade cidade;
}
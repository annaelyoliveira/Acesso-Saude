package acessosaude.model;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "\"tb_cidades\"")
@Data
public class Cidade {
    @Id
    @Column(name = "\"CO_IBGE\"")
    private String coIbge; // Garanta que é String
    
    @Column(name = "\"NO_MUNICIPIO\"")
    private String nome;
}
package acessosaude.model;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "turno")
@Data
public class Turno {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String descricao;
}
package acessosaude.controller;

import acessosaude.model.Unidade;
import acessosaude.repository.UnidadeRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/acesso-saude")
public class UnidadeController {

    @Autowired
    private UnidadeRepository repository;

    @GetMapping("/por-turno")
    public List<Unidade> listarPorTurno(@RequestParam String valor) {
        return repository.findByTurnoDescricaoContainingIgnoreCase(valor);
    }

    @GetMapping("/por-tipo")
    public List<Unidade> listarPorTipo(@RequestParam String valor) {
        return repository.findByTpUnidadeContainingIgnoreCase(valor);
    }

    @GetMapping("/por-localizacao")
    public List<Unidade> listarPorLocal(
            @RequestParam String cidade,
            @RequestParam String bairro) {
        return repository.findByEnderecoCidadeNomeIgnoreCaseAndEnderecoBairroIgnoreCase(cidade, bairro);
    }

    @GetMapping("/todas")
    public List<Unidade> listarTodas() {
        return repository.findAll();
    }
}
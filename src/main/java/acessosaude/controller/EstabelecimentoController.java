package acessosaude.controller;

import acessosaude.model.Estabelecimento;
import acessosaude.repository.EstabelecimentoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/estabelecimentos")
public class EstabelecimentoController {

    @Autowired
    private EstabelecimentoRepository repository;

    @GetMapping("/turno")
    public List<Estabelecimento> buscarPorTurno(@RequestParam String valor) {
        return repository.findByTurnoAtendimentoContainingIgnoreCase(valor);
    }

    @GetMapping("/tipo")
    public List<Estabelecimento> buscarPorTipo(@RequestParam String valor) {
        return repository.findByTpUnidadeContainingIgnoreCase(valor);
    }

    @GetMapping("/localizacao")
    public List<Estabelecimento> buscarPorLocal(
            @RequestParam String cidade,
            @RequestParam String bairro) {
        return repository.findByEnderecoCidadeIgnoreCaseAndEnderecoBairroIgnoreCase(cidade, bairro);
    }

    @GetMapping
    public List<Estabelecimento> listarTodos() {
        return repository.findAll();
    }
}
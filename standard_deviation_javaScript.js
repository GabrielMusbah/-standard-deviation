function desvioPadrao (lista){

    let listaSplit = lista.split(" ");
    
    let listaInt = listaSplit.map(Number);
    
    let media = listaInt.reduce((soma, valor) => soma += valor, 0) / listaInt.length;
    
    let listaMenosMedia = listaInt.map(num => {
        return num - media;
    });
    
    let listaQuadrado = listaMenosMedia.map(num => {
        return num ** 2;
    });
    
    let somaLista = listaQuadrado.reduce((soma, valor) => soma += valor, 0);
    
    let somaListaSobQuantidade = somaLista / (listaInt.length - 1);
    
    let raiz = Math.sqrt(somaListaSobQuantidade);
    
    //console.log(raiz.toFixed(3));
    
    return raiz
    }
    
    let lista = "1 2 3 4 5 6 7 8 9 10";
    
    let desvio = desvioPadrao(lista)
    
    console.log(desvio.toFixed(4))

public class q3_A {
    public static void main(String[] args) {
        int[][][] img = ImagemDigital.carregarImagemCor("semana 8/laisy.jpeg");
        // Dimensão da foto menor
        int[][][] img2 = new int[150][150][3];

        ImagemDigital.plotarImagemCor(img, "Imagem I");

        for(int x = 0; x < img.length; x++){
            // Intervalo do eixo X
            if (x > 300 && x < 450){
                img2[x-300] = img[x];
            for(int y = 0; y < img[x].length; y++){
                // Intervalo do eixo Y
                if (y > 600 && y < 750){
                    img2[x-300][y-600] = img[x][y];
                    for(int z = 0; z< img[x][y].length; z++){
                        img2[x-300][y-600][z] = img[x][y][z];
                    }
                }
            }
                            
            }
        }

        ImagemDigital.plotarImagemCor(img2, "Imagem II");
    }

}
public class q3_B {
    public static void main(String[] args) {
        int[][][] img = ImagemDigital.carregarImagemCor("semana 8/laisy.jpeg");
        int[][][] img2 = new int[150][150][3];
        int aux = 0;

        ImagemDigital.plotarImagemCor(img, "Imagem I");

        for(int x = 0; x < img.length; x++){
            if (x > 300 && x < 450){
                img2[x-300] = img[x];
            for(int y = 0; y < img[x].length; y++){
                if (y > 600 && y < 750){
                    img2[x-300][y-600] = img[x][y];
                    for(int z = 0; z< img[x][y].length; z++){
                        if(z == 2){
                            aux = img[x][y][z];
                            img2[x-300][y-600][z] = Math.min(254, aux+120);                        }
                        
                    }
                }
            }                                          
            }
        }

        ImagemDigital.plotarImagemCor(img2, "Imagem II");
    }
}

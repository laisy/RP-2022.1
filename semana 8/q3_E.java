public class q3_E {
    public static void main(String[] args) {
        int[][][] img = ImagemDigital.carregarImagemCor("semana 8/laisy.jpeg");
        int[][][] img2 = new int[150][150][3];
        int aux = 0;
        int aux_int = 0;

        ImagemDigital.plotarImagemCor(img, "Imagem I");

        for(int x = 0; x < img.length; x++){
            if (x > 300 && x < 450){
                img2[x-300] = img[x];
            for(int y = 0; y < img[x].length; y++){
                if (y > 600 && y < 750){
                    img2[x-300][y-600] = img[x][y];
                    for(int z = 0; z< img[x][y].length; z++){
                        aux = img[x][y][z];
                        double aux_double = (double) aux * 1.9;
                        aux_int = (int) Math.round(aux_double);
                        img2[x-300][y-600][z] = Math.min(255, aux_int);             
                        }
                    }
                }                                          
            }
        }
        ImagemDigital.plotarImagemCor(img2, "Imagem II");    }
}    
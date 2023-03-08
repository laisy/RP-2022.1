public class q2 {
    public static int[] q1(int[][] imagem){
        int[] pixel_list = new int[7200];
        for(int i = 0; i < imagem.length; i++){
            for(int j = 0; j < imagem[0].length; j++){
                pixel_list[i] = imagem[i][j];
            }

        }

		return pixel_list;
	}

	public static void printarPixels(int[] pixel_list){
		int aux = 0;
		for(int u = 0; u < pixel_list.length; u++){
            if(pixel_list[u] != aux){
                System.out.print("[");
                System.out.print(pixel_list[u]);
                System.out.print("] ");
                aux = pixel_list[u];
            }
            
        }
	}
    public static void main(String[] args) {
        int[][] img = new int[300][300];

        System.out.print("imagem I: ");
        for(int i = 0; i < img.length; i++){
            for(int j = 0; j < img[0].length; j++){
                // Construção do quadrado interno
                if((j > 100 && j < 200) && (i > 100 && i < 200)){
                    // Intensidade do quadrado do centro
                    img[i][j] = 128;
                }
                // Intensidade do quadrado do fundo
                else{
                    img[i][j] = 0;
                }
            }


        }

        ImagemDigital.plotarImagem(img, "imagem I");

        System.out.print("imagem II: ");
        for(int i = 0; i < img.length; i++){
            for(int j = 0; j < img[0].length; j++){
                 // Construção do quadrado interno
                if((j > 100 && j < 200) && (i > 100 && i < 200)){
                    // Intensidade do quadrado do centro
                    img[i][j] = 128;
                }
                 // Intensidade do quadrado do fundo
                else{
                    img[i][j] = 64;
                }
            }

        }

        ImagemDigital.plotarImagem(img, "imagem II");

        System.out.print("imagem III: ");
        for(int i = 0; i < img.length; i++){
            // Construção do quadrado interno
            for(int j = 0; j < img[0].length; j++){
                if((j > 100 && j < 200) && (i > 100 && i < 200)){
                    // Intensidade do quadrado do centro
                    img[i][j] = 128;
                }
                 // Intensidade do quadrado do fundo
                else{
                    img[i][j] = 192;
                }
            }

        }
        ImagemDigital.plotarImagem(img, "imagem III");
    }
}

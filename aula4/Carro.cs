namespace projeto
{
    public class Carro
    {
        public bool ChaveAtiva {  get; private set; } = false;
        public  int Velocidade { get; private set; } = 0;
        public bool portasAbertas { get; private set; } = false;

        public void Abrir()
        {
            portasAbertas = true;
            AtivarChaveSeAberto();
        }
        public void Fechar()
        {
            portasAbertas = false;
        }
        private void AtivarChaveSeAberto()
        {
            if (portasAbertas)
            {
                ChaveAtiva = true;
                Console.WriteLine("Chave ativada");
            }
        }

        public void Acelerar(int incremento)
        {
            if (incremento > 0)
            {
                Velocidade += incremento;
                Console.WriteLine($"Acelerando. Velocidade atual: {Velocidade} km/h");
            }
            
        }

        public void Freia()
        {
            if (Velocidade > 0)
            {
                Velocidade -= 5;
                if (Velocidade < 0)
                    Velocidade = 0;
                Console.WriteLine($"Freando. velocidade atual: {Velocidade} km/h");
            }
            else
            {
                Console.WriteLine("O carro esta parado.");
            }
        }

        public void Desligar()
        {
            if(Velocidade == 0)
            {
                ChaveAtiva = false;
                Console.WriteLine("Carro desligado");
            }
            else
            {
                Console.WriteLine("Não é possivel desligar o carro enquanto estiver acelerado.");
            }
        }
    }

    public class Apresentar
    {
        static void Main(string[] args)
        {
            Carro meuCarro = new Carro();

            meuCarro.Abrir();
            meuCarro.Acelerar(20);
            meuCarro.Freia();
            meuCarro.Freia();
            meuCarro.Freia();
            meuCarro.Freia();
            meuCarro.Desligar();
        }
    }
}


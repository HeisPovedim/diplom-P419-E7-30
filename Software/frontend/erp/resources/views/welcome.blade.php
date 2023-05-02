<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href='/css/style.css'>
    <title>E7 - 30</title>
</head>
<body>
    <header>
        <p>header</p>
    </header>
            <main>
            <div class="loading">
            <div class="loading-text">Please wait...</div>
                <div class="loading-circle"></div>
            </div>
                </div>
                    <div class="conteiner">
                        <form action="/start" method="post" class="form">
                        @csrf
                        <input type="number" name="f_start" placeholder="f_start" required value=1750000 /> <!-- required -->
                        <input type="number" name="f_end" placeholder="f_end" value=1760000 required/>
                        <input type="number" name="step" placeholder="step" required value=10000 /><br>
                        <div class="check_box">
                            <label for="z_only">Передать параметр z_only: </label>
                            <input type="checkbox" name="z_only" placeholder="z_only" />
                        </div>

                        <input type="submit" class="btn_back" onclick="showLoading()">
                        </form>
                    </div>
            </main>
    <footer>
        <p>Footer</p>
    </footer>
</body>
<script type="text/javascript">
    function showLoading() {
        document.querySelector('.loading').style.display = "block";
        document.querySelector('.conteiner').style.display = "none";
        main = document.querySelector('.img').classList.add('addimg');
    }
</script>
</html>
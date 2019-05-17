<!doctype html>
<html lang="pl">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Justyna Kusal">
    <meta name="generator" content="Jekyll v3.8.5">
    <title><?php get_page_clean_title(); ?> &lt; <?php get_site_name(); ?></title>


    <!-- Bootstrap core CSS -->
<link href="<?php get_theme_url(); ?>/css/bootstrap.min.css" rel="stylesheet">


    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
    </style>
    <!-- Custom styles for this template -->
    <link href="<?php get_theme_url(); ?>/style.css" rel="stylesheet">
    <?php get_header(); ?>
  </head>
  <body>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark">
  <a class="navbar-brand" href="<?php get_site_url(); ?>"><?php get_site_name(); ?></a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarsExampleDefault">
    <ul class="navbar-nav mx-auto">
        <?php get_navigation(return_page_slug()); ?>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">
      <button class="btn btn-secondary my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>

<main role="main" class="container">
    <div class="row">
        <div class="col-sm-8">
            <h1><?php get_page_clean_title(); ?></h1>
            <?php get_page_content(); ?>
        </div>
        
        <div class="col-sm-4">
            <?php get_component('sidebar'); ?>
        </div>
    
    </div>

  <div class="starter-template">
    <h1>Bootstrap starter template</h1>
    <p class="lead">Use this document as a way to quickly start any new project.<br> All you get is this text and a mostly barebones HTML document.</p>
  </div>

</main><!-- /.container -->

    <div class="container">
        <div class="row">
            <div class="col">
            <?php get_footer(); ?>
            </div>
        </div>
    </div>
    
<script <?php get_theme_url(); ?>/js/jquery.min.js></script>
<script <?php get_theme_url(); ?>/js/popper.min.js></script>
<script <?php get_theme_url(); ?>/js/bootstrap.min.js></script>
      <script>window.jQuery || document.write('<script src="/docs/4.3/assets/js/vendor/jquery-slim.min.js"><\/script>')</script><script src="/docs/4.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-xrRywqdh3PHs8keKZN+8zzc5TX0GRTLCcmivcbNJWm2rs5C8PRhcEn3czEjhAO9o" crossorigin="anonymous"></script></body>
</html>


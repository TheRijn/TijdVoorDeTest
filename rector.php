<?php

declare(strict_types=1);

use Rector\Config\RectorConfig;

return RectorConfig::configure()
    ->withPaths([
        __DIR__.'/config',
        __DIR__.'/public',
        __DIR__.'/src',
        __DIR__.'/tests',
    ])
    ->withPhpSets()
    ->withPreparedSets(deadCode: true, codeQuality: true, codingStyle: true, typeDeclarations: true, privatization: true, instanceOf: true, earlyReturn: true, strictBooleans: true, phpunitCodeQuality: true, doctrineCodeQuality: true, symfonyCodeQuality: true)
    ->withComposerBased(twig: true, doctrine: true, phpunit: true);

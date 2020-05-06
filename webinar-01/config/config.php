<?php  // Moodle configuration file

unset($CFG);
global $CFG;
$CFG = new stdClass();

$CFG->dbtype    = 'mysqli';
$CFG->dblibrary = 'native';
$CFG->dbhost    = '<your rds endpoint>';
$CFG->dbname    = 'bitnami_moodle';
$CFG->dbuser    = 'bn_moodle';
$CFG->dbpass    = 'fdf8f7aefc';
$CFG->prefix    = 'mdl_';
$CFG->dboptions = array(
    'dbpersist' => 0,
    'dbport' => 3306,
    'dbsocket' => 0,
    'dbcollation' => 'utf8_general_ci',
);

// Hostname definition //
$hostname = 'moodle.awsunicorn.com';
$hostwithprotocol = 'https://' . strtolower($hostname);
$CFG->wwwroot = strtolower($hostwithprotocol);
$CFG->sslproxy = (substr($hostwithprotocol, 0, 5) == 'https' ? true : false);

// Moodledata location //
$CFG->dataroot  = '/opt/bitnami/apps/moodle/data';
$CFG->tempdir = '/opt/bitnami/apps/moodle/temp';
$CFG->cachedir = '/opt/bitnami/apps/moodle/cache';
$CFG->localcachedir = '/opt/bitnami/apps/moodle/local';
$CFG->admin     = 'admin';
$CFG->directorypermissions = 02777;

// Configure Session Cache
$CFG->dbsessions = 0;
$CFG->session_handler_class = '\core\session\memcached';
$CFG->session_memcached_save_path = '<your elasticache endpoint>:11211';
$CFG->session_memcached_prefix = 'memc.sess.key.';
$CFG->session_memcached_acquire_lock_timeout = 120;
$CFG->session_memcached_lock_expire = 7100;
$CFG->session_memcached_lock_retry_sleep = 150;

require_once(__DIR__ . '/lib/setup.php');

// There is no php closing tag in this file,
// it is intentional because it prevents trailing whitespace problems!

-- phpMyAdmin SQL Dump
-- version 3.3.2deb1ubuntu1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Erstellungszeit: 17. Dezember 2012 um 14:23
-- Server Version: 5.1.66
-- PHP-Version: 5.3.2-1ubuntu4.18

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Datenbank: `vamos`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `zeiteinheiten`
--

CREATE TABLE IF NOT EXISTS `zeiteinheiten` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `einheit` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `inminuten` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Daten für Tabelle `zeiteinheiten`
--

INSERT INTO `zeiteinheiten` (`id`, `einheit`, `inminuten`) VALUES
(1, 'Minute', 1),
(2, 'Minuten', 1),
(3, 'Stunde', 60),
(4, 'Stunden', 60),
(5, 'Tag', 1440),
(6, 'Tage', 1440),
(7, 'Dreiviertelstunde', 45),
(8, 'Viertelstunde', 15),
(9, 'Std.', 60),
(10, 'Std', 60),
(11, 'min.', 1),
(12, 'min', 1);

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
-- Tabellenstruktur für Tabelle `zeitquantitaeten`
--

CREATE TABLE IF NOT EXISTS `zeitquantitaeten` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantitaet` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `faktor` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=29 ;

--
-- Daten für Tabelle `zeitquantitaeten`
--

INSERT INTO `zeitquantitaeten` (`id`, `quantitaet`, `faktor`) VALUES
(1, 'halbe', 0.5),
(2, 'viertel', 0.25),
(3, 'dreiviertel', 0.75),
(4, 'ein', 1),
(5, 'eine', 1),
(6, 'zwei', 2),
(7, 'drei', 3),
(8, 'vier', 4),
(9, 'fünf', 5),
(10, 'sechs', 6),
(11, 'sieben', 7),
(12, 'acht', 8),
(13, 'neun', 9),
(14, 'zehn', 10),
(15, 'elf', 11),
(16, 'zwölf', 12),
(17, 'dreizehn', 13),
(18, 'eineinhalb', 1.5),
(19, 'eineinviertel', 1.25),
(20, 'zweieinhalb', 2.5),
(21, 'dreieinhalb', 3.5),
(22, 'viereinhalb', 4.5),
(23, 'fünfeinhalb', 5.5),
(24, 'sechseinhalb', 6.5),
(25, 'siebeneinhalb', 7.5),
(26, 'achteinhalb', 8.5),
(27, 'paar', 5),
(28, 'einige', 5);

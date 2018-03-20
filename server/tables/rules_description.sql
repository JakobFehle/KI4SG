-- phpMyAdmin SQL Dump
-- version 3.3.2deb1ubuntu1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Erstellungszeit: 17. Dezember 2012 um 14:22
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
-- Tabellenstruktur für Tabelle `rules_description`
--

CREATE TABLE IF NOT EXISTS `rules_description` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `suche` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `ersetze` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=25 ;

--
-- Daten für Tabelle `rules_description`
--

INSERT INTO `rules_description` (`id`, `suche`, `ersetze`) VALUES
(1, 'eier', 'ei'),
(2, 'eiweiß', 'ei'),
(3, 'eigelb', 'ei'),
(4, 'Eigelbe', 'ei'),
(5, 'Eischnee', 'ei'),
(6, 'Eiklar', 'ei'),
(7, 'Eiercreme', 'ei'),
(8, 'Eigelbmasse', 'ei'),
(9, 'Eidotter', 'ei'),
(10, 'Eischnees', 'ei'),
(11, 'Risottoreis', 'reis'),
(12, 'frühlingszwiebeln', 'frühlingszwiebel'),
(13, 'Pilze', 'pilze champignons'),
(14, 'Olivenöl', 'öl'),
(15, 'Knobi', 'knoblauch'),
(16, 'Teigs', 'Teig'),
(17, 'Teighälfte', 'Teig'),
(18, 'Fleischmasse', 'fleisch'),
(19, 'Keulen', 'keule'),
(20, 'Langkornreis', 'reis'),
(21, 'eiklar', 'ei'),
(22, 'eidotter', 'ei'),
(23, 'eiern', 'ei'),
(24, 'dotter', 'ei');

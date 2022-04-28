--
-- PostgreSQL database dump
--

-- Dumped from database version 13.6 (Debian 13.6-1.pgdg110+1)
-- Dumped by pg_dump version 13.6 (Debian 13.6-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: geostore; Type: SCHEMA; Schema: -; Owner: geostore
--

CREATE USER geostore with password 'geostore';

CREATE SCHEMA geostore;


ALTER SCHEMA geostore OWNER TO geostore;

--
-- Name: geostore_test; Type: SCHEMA; Schema: -; Owner: geostore
--

CREATE SCHEMA geostore_test;


ALTER SCHEMA geostore_test OWNER TO geostore;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: gs_attribute; Type: TABLE; Schema: geostore; Owner: geostore
--

CREATE TABLE geostore.gs_attribute (
    id bigint NOT NULL,
    attribute_date timestamp without time zone,
    name character varying(255) NOT NULL,
    attribute_number double precision,
    attribute_text character varying(255),
    attribute_type character varying(255) NOT NULL,
    resource_id bigint NOT NULL
);


ALTER TABLE geostore.gs_attribute OWNER TO geostore;

--
-- Name: gs_category; Type: TABLE; Schema: geostore; Owner: geostore
--

CREATE TABLE geostore.gs_category (
    id bigint NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE geostore.gs_category OWNER TO geostore;

--
-- Name: gs_resource; Type: TABLE; Schema: geostore; Owner: geostore
--

CREATE TABLE geostore.gs_resource (
    id bigint NOT NULL,
    creation timestamp without time zone NOT NULL,
    description character varying(10000),
    lastupdate timestamp without time zone,
    metadata character varying(30000),
    name character varying(255) NOT NULL,
    category_id bigint NOT NULL
);


ALTER TABLE geostore.gs_resource OWNER TO geostore;

--
-- Name: gs_security; Type: TABLE; Schema: geostore; Owner: geostore
--

CREATE TABLE geostore.gs_security (
    id bigint NOT NULL,
    canread boolean NOT NULL,
    canwrite boolean NOT NULL,
    group_id bigint,
    resource_id bigint,
    user_id bigint,
    username character varying(255),
    groupname character varying(255)
);


ALTER TABLE geostore.gs_security OWNER TO geostore;

--
-- Name: gs_stored_data; Type: TABLE; Schema: geostore; Owner: geostore
--

CREATE TABLE geostore.gs_stored_data (
    id bigint NOT NULL,
    stored_data character varying(10000000) NOT NULL,
    resource_id bigint NOT NULL
);


ALTER TABLE geostore.gs_stored_data OWNER TO geostore;

--
-- Name: gs_user; Type: TABLE; Schema: geostore; Owner: geostore
--

CREATE TABLE geostore.gs_user (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    user_password character varying(255),
    user_role character varying(255) NOT NULL,
    group_id bigint,
    enabled character(1) DEFAULT 'Y'::bpchar NOT NULL
);


ALTER TABLE geostore.gs_user OWNER TO geostore;

--
-- Name: gs_user_attribute; Type: TABLE; Schema: geostore; Owner: geostore
--

CREATE TABLE geostore.gs_user_attribute (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    string character varying(255),
    user_id bigint NOT NULL
);


ALTER TABLE geostore.gs_user_attribute OWNER TO geostore;

--
-- Name: gs_usergroup; Type: TABLE; Schema: geostore; Owner: geostore
--

CREATE TABLE geostore.gs_usergroup (
    id bigint NOT NULL,
    groupname character varying(255) NOT NULL,
    description character varying(255),
    enabled character(1) DEFAULT 'Y'::bpchar NOT NULL
);


ALTER TABLE geostore.gs_usergroup OWNER TO geostore;

--
-- Name: gs_usergroup_members; Type: TABLE; Schema: geostore; Owner: geostore
--

CREATE TABLE geostore.gs_usergroup_members (
    user_id bigint NOT NULL,
    group_id bigint NOT NULL
);


ALTER TABLE geostore.gs_usergroup_members OWNER TO geostore;

--
-- Name: hibernate_sequence; Type: SEQUENCE; Schema: geostore; Owner: geostore
--

CREATE SEQUENCE geostore.hibernate_sequence
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE geostore.hibernate_sequence OWNER TO geostore;

--
-- Name: gs_attribute; Type: TABLE; Schema: geostore_test; Owner: geostore
--

CREATE TABLE geostore_test.gs_attribute (
    id bigint NOT NULL,
    attribute_date timestamp without time zone,
    name character varying(255) NOT NULL,
    attribute_number double precision,
    attribute_text character varying(255),
    attribute_type character varying(255) NOT NULL,
    resource_id bigint NOT NULL
);


ALTER TABLE geostore_test.gs_attribute OWNER TO geostore;

--
-- Name: gs_category; Type: TABLE; Schema: geostore_test; Owner: geostore
--

CREATE TABLE geostore_test.gs_category (
    id bigint NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE geostore_test.gs_category OWNER TO geostore;

--
-- Name: gs_resource; Type: TABLE; Schema: geostore_test; Owner: geostore
--

CREATE TABLE geostore_test.gs_resource (
    id bigint NOT NULL,
    creation timestamp without time zone NOT NULL,
    description character varying(10000),
    lastupdate timestamp without time zone,
    metadata character varying(30000),
    name character varying(255) NOT NULL,
    category_id bigint NOT NULL
);


ALTER TABLE geostore_test.gs_resource OWNER TO geostore;

--
-- Name: gs_security; Type: TABLE; Schema: geostore_test; Owner: geostore
--

CREATE TABLE geostore_test.gs_security (
    id bigint NOT NULL,
    canread boolean NOT NULL,
    canwrite boolean NOT NULL,
    group_id bigint,
    resource_id bigint,
    user_id bigint,
    username character varying(255),
    groupname character varying(255)
);


ALTER TABLE geostore_test.gs_security OWNER TO geostore;

--
-- Name: gs_stored_data; Type: TABLE; Schema: geostore_test; Owner: geostore
--

CREATE TABLE geostore_test.gs_stored_data (
    id bigint NOT NULL,
    stored_data character varying(10000000) NOT NULL,
    resource_id bigint NOT NULL
);


ALTER TABLE geostore_test.gs_stored_data OWNER TO geostore;

--
-- Name: gs_user; Type: TABLE; Schema: geostore_test; Owner: geostore
--

CREATE TABLE geostore_test.gs_user (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    user_password character varying(255),
    user_role character varying(255) NOT NULL,
    group_id bigint,
    enabled character(1) DEFAULT 'Y'::bpchar NOT NULL
);


ALTER TABLE geostore_test.gs_user OWNER TO geostore;

--
-- Name: gs_user_attribute; Type: TABLE; Schema: geostore_test; Owner: geostore
--

CREATE TABLE geostore_test.gs_user_attribute (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    string character varying(255),
    user_id bigint NOT NULL
);


ALTER TABLE geostore_test.gs_user_attribute OWNER TO geostore;

--
-- Name: gs_usergroup; Type: TABLE; Schema: geostore_test; Owner: geostore
--

CREATE TABLE geostore_test.gs_usergroup (
    id bigint NOT NULL,
    groupname character varying(255) NOT NULL,
    description character varying(255),
    enabled character(1) DEFAULT 'Y'::bpchar NOT NULL
);


ALTER TABLE geostore_test.gs_usergroup OWNER TO geostore;

--
-- Name: gs_usergroup_members; Type: TABLE; Schema: geostore_test; Owner: geostore
--

CREATE TABLE geostore_test.gs_usergroup_members (
    user_id bigint NOT NULL,
    group_id bigint NOT NULL
);


ALTER TABLE geostore_test.gs_usergroup_members OWNER TO geostore;

--
-- Name: hibernate_sequence; Type: SEQUENCE; Schema: geostore_test; Owner: geostore
--

CREATE SEQUENCE geostore_test.hibernate_sequence
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE geostore_test.hibernate_sequence OWNER TO geostore;

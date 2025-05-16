import {
  AfterViewInit,
  ChangeDetectionStrategy,
  Component,
  ElementRef,
  ViewChild,
  Inject,
  PLATFORM_ID,
  OnDestroy,
  Input,
  TemplateRef,
} from '@angular/core';
import { Router } from '@angular/router';
import { isPlatformBrowser } from '@angular/common';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Color, Map, Marker } from 'maplibre-gl';
import { environment } from '../../../../environments/environment';
import { RealEstateProperty } from '../../interfaces/realEstateProperty';
import { map } from 'rxjs';
import { DetailsComponent } from '../details/details.component';
import { DetailModalComponent } from '../detail-modal/detail-modal.component';

@Component({
  selector: 'app-map',
  standalone: true,
  imports: [DetailsComponent],
  templateUrl: './map.component.html',
  styleUrl: './map.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class MapComponent implements AfterViewInit, OnDestroy {
  map: Map | undefined;
  @ViewChild('map', { static: false }) mapContainer?: ElementRef<HTMLElement>;
  @Input() properties: RealEstateProperty[] | null = null;
  selectedProperty: RealEstateProperty | null = null;

  public markers: Marker[] = [];

  constructor(
    @Inject(PLATFORM_ID) private platformId: any,
    private modalService: NgbModal
  ) {}

  ngAfterViewInit(): void {
    if (isPlatformBrowser(this.platformId)) {
      const initialState = { lng: -80.34599, lat: 25.7578, zoom: 10 };

      if (!this.mapContainer) throw 'HTML Element not found';

      this.map = new Map({
        container: this.mapContainer.nativeElement,
        style: `https://api.maptiler.com/maps/streets-v2/style.json?key=${environment.maplibre_key}`,
        center: [initialState.lng, initialState.lat],
        zoom: initialState.zoom,
      });

      this.map.on('load', () => {
        // Asegurarse de que el mapa está cargado antes de añadir marcadores
        if (this.properties) {
          this.properties.forEach((property) => this.createMarker(property));
        }
      });

      // 🔹 Forzar redibujado después de un breve delay
      setTimeout(() => {
        this.map?.resize();
      }, 500);
    }
  }

  createMarker(property: RealEstateProperty) {
    let color: string = 'red';
    // check the colors of markers
    if (property.price_decrease === true) {
      color = 'yellow';
    }
    if (property.new === true) {
      color = 'blue';
    }
    // call the marker
    this.addMarker(property.lon, property.lat, color, property);
    console.log('createmarker');
  }

  addMarker(
    lng: number,
    lat: number,
    color: string = 'red',
    property?: RealEstateProperty
  ) {
    if (!this.map) return;

    const el = document.createElement('div');
    el.className = 'custom-marker';
    el.style.backgroundColor = color;
    el.style.width = '24px';
    el.style.height = '24px';
    el.style.borderRadius = '50%';
    el.style.cursor = 'pointer';
    el.style.border = '2px solid white';

    if (property) {
      el.title = `${property.title} - $${property.price}`; // fallback tooltip
    }

    // ➕ Popover manual
    el.addEventListener('mouseenter', () => {
      const popover = document.createElement('div');
      popover.className = 'custom-popover';
      popover.innerHTML = `
        <strong>${property?.title}</strong><br>
        $${property?.price}
      `;
      document.body.appendChild(popover);

      const rect = el.getBoundingClientRect();
      popover.style.left = `${rect.left + rect.width / 2}px`;
      popover.style.top = `${rect.top - 40}px`;
      popover.style.position = 'fixed';
      popover.style.backgroundColor = 'white';
      popover.style.padding = '6px 10px';
      popover.style.border = '1px solid #ccc';
      popover.style.borderRadius = '4px';
      popover.style.boxShadow = '0 2px 8px rgba(0,0,0,0.15)';
      popover.style.zIndex = '1000';

      el.addEventListener(
        'mouseleave',
        () => {
          popover.remove();
        },
        { once: true }
      );
    });

    // ➕ Click para navegar
    el.addEventListener('click', () => {
      if (property) {
        const modalRef = this.modalService.open(DetailModalComponent, {
          size: 'xl',
        });
        modalRef.componentInstance.property = property;
      }
    });

    const marker = new Marker({ element: el })
      .setLngLat([lng, lat])
      .addTo(this.map);

    this.markers.push(marker);
  }

  ngOnDestroy() {
    this.map?.remove();
  }
}
